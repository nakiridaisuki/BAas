from module.base.base import ModuleBase
from module.base.decorator import run_once
from module.logger import logger
from module.exception import GameNotRunningError, GamePageUnknownError, ScriptError, TaskError
from module.base.timer import Timer
from module.base.utils import *
from module.ocr.ocr import Digit, Ocr, DigitCounter, OcrWhiteLetterOnComplexBackground
from tasks.base.assets.assets_base_page import *
from tasks.base.assets.assets_base_ui import *
from tasks.base.page import Page

class WhiteDigit(OcrWhiteLetterOnComplexBackground):
    def __init__(self, button: ButtonWrapper, lang=None, name=None):
        super().__init__(button, lang=lang, name=name)

    def format_result(self, result) -> int:
        """
        Returns:
            int:
        """
        result = super().after_process(result)
        logger.attr(name=self.name, text=str(result))

        res = re.search(r'(\d+)', result)
        if res:
            return int(res.group(1))
        else:
            logger.warning(f'No digit found in {result}')
            return 0

class UI(ModuleBase):

    def color_appear_then_click(self, button, interval=3, threshold=10):
        if self.match_color(button, interval=interval, threshold=threshold):
            self.device.click(button)
            return True
        return False
    
    def color_appear(self, button, interval=3, threshold=10):
        return self.match_color(button, interval=interval, threshold=threshold)
    
    def ui_page_appear(self, page: Page, interval=0):
        return self.appear(page.check_button, interval=interval)
    
    def ui_get_current_page(self, skip_first_screenshot=True):
        """
        Args:
            skip_first_screenshot:

        Returns:
            Page:

        Raises:
            GameNotRunningError:
            GamePageUnknownError:
        """
        logger.info("UI get current page")

        @run_once
        def app_check():
            if not self.device.app_is_running():
                raise GameNotRunningError("Game not running")

        @run_once
        def minicap_check():
            if self.config.Emulator_ControlMethod == "uiautomator2":
                self.device.uninstall_minicap()

        @run_once
        def rotation_check():
            self.device.get_orientation()

        timeout = Timer(10, count=20).start()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
                if not hasattr(self.device, "image") or self.device.image is None:
                    self.device.screenshot()
            else:
                self.device.screenshot()

            # End
            if timeout.reached():
                break

            # Known pages
            for page in Page.iter_pages():
                if page.check_button is None:
                    continue
                if self.ui_page_appear(page=page):
                    logger.attr("UI", page.name)
                    self.ui_current = page
                    return page

            # Unknown page but able to handle
            if self.ui_touch():
                continue

            app_check()
            minicap_check()
            rotation_check()

        # Unknown page, need manual switching
        logger.warning("Unknown ui page")
        logger.attr("EMULATOR__SCREENSHOT_METHOD", self.config.Emulator_ScreenshotMethod)
        logger.attr("EMULATOR__CONTROL_METHOD", self.config.Emulator_ControlMethod)
        logger.attr("Lang", self.config.LANG)
        logger.warning("Starting from current page is not supported")
        logger.warning(f"Supported page: {[str(page) for page in Page.iter_pages()]}")
        logger.warning('Supported page: Any page with a "HOME" button on the upper-right')
        logger.critical("Please switch to a supported page before starting SRC")
        raise GamePageUnknownError
    
    def ui_goto(self, destination: Page, skip_first_screenshot=True):
        """
        Need screenshot first or set skip_first_screenshot to False
        Args:
            destination (Page):
            skip_first_screenshot:
        """

        # Find the path
        Page.init_connection(destination)
        self.interval_clear(list(Page.iter_check_buttons()))

        logger.hr(f"UI goto {destination}")
        unknow_timer = Timer(5)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            # Destination page
            if self.ui_page_appear(destination):
                # self.device.image_show()
                logger.info(f'Page arrive: {destination}')
                break

            # Other pages
            clicked = False
            for page in Page.iter_pages():
                if page.parent is None or page.check_button is None:
                    continue

                if self.ui_page_appear(page, interval=1.5):
                    logger.info(f'Page switch: {page} -> {page.parent}')
                    button = page.links[page.parent]
                    self.device.click(button)
                    clicked = True
                    break
            if clicked:
                unknow_timer.reset()
                continue

            # Additional
            if unknow_timer.reached():
                self.ui_touch()
                unknow_timer.reset()
                continue

        # Reset connection
        Page.clear_connection()

    def ui_ensure(self, destination, skip_first_screenshot=False):
        """
        Args:
            destination (Page):
            acquire_lang_checked:
            skip_first_screenshot:

        Returns:
            bool: If UI switched.
        """
        logger.hr("UI ensure")
        self.ui_get_current_page(skip_first_screenshot=skip_first_screenshot)

        if self.ui_current == destination:
            logger.info("Already at %s" % destination)
            return False
        else:
            logger.info("Goto %s" % destination)
            self.ui_goto(destination, skip_first_screenshot=True)
            return True

    reward_timer = Timer(2)
    def ui_reward_acquired(self, interval=2):
        """
        Handle reward acquired page
        The page has TOUCH word
        """
        if not self.reward_timer.reached():
            return False
        
        self.reward_timer = Timer(interval).start()
        ocr = Ocr(REWARD_ACQUIRED)
        result = ocr.ocr_single_line(self.device.image)
        if result == 'TOUCH':
            logger.info('Reward acquired')
            self.device.click(REWARD_ACQUIRED)
            return True
        return False

    touch_timer = Timer(5)
    def ui_touch(self, interval=5):
        """
        Try to leave from unknow page, it's usually work
        """
        if self.touch_timer.reached():
            logger.info('Handle unknow page by click home button')
            self.device.click(GOTO_MAIN)
            self.touch_timer = Timer(interval).start()
        return True
    
    def ui_get_AP(self, skip_first_screenshot=False):
        if skip_first_screenshot:
            skip_first_screenshot = True
        else:
            self.device.screenshot()

        if self.appear(PAGE_MAIN):
            from tasks.base.page import page_campaign
            self.ui_goto(page_campaign)

        ocr = DigitCounter(AP_AREA)
        retry = Timer(2)
        timeout = Timer(300).start()
        while 1:
            if retry.reached():
                retry.reset()
                self.device.screenshot()
                ap, remain, total = ocr.ocr_single_line(self.device.image)
                if total == 0:
                    continue
                return ap
            if timeout.reached():
                logger.error('UI get AP faild')
                raise TaskError
    
    def ui_find_level(self, area=None, in_mission=False, keyword='1-1'):
        """
        Find maximum or specific level which can be swept

        Args:
            area: (ButtonWrapper) the area you want find
            in_mission: (bool) if you are in mission
            keyword: (str) mission id

        Return: A Tuple: (a enter button with offset if finded or None 
                          , if it's current maximum level)
                or just a button if in mission is True
        """
        if area is None:
            logger.error('Need area argument')
            raise ScriptError
        
        ocr = Ocr(area)
        self.device.screenshot()
        result = ocr.detect_and_ocr(self.device.image)
        idx = 0
        for level in result[::-1]:
            if in_mission and level.ocr_text != keyword:
                continue

            idx += 1
            x1, y1, x2, y2 = level.box
            m = (x1 + x2) // 2
            x1 = m - 30
            x2 = m + 30
            y2 += 30
            image = crop(self.device.image, (x1, y1, x2, y2))
            if STARS_3.match_template(image, similarity=0.7, direct_match=True):
                button = ENTER
                button.clear_offset()
                button.buttons[0]._button_offset = (x1 - (button.button[0] - 390), y1 - button.button[1])

                if in_mission:
                    button.name = 'MISSION_' + keyword
                    return button
                
                button.name = f'LEVEL_{int(level.ocr_text)}'
                return button, idx < 3
        return None

    def ui_scroll(self, vector=(0, 0), swipe_area=None, duration=(0.1, 0.2)):
        """
        Args:
            vector: (tuple) direction you want to swipe, auto scale to swip_area
            swipe_area: (ButtonWrapper)
            duration: (tuple)
        """
        if swipe_area is None or vector == (0, 0):
            raise ScriptError
        if not isinstance(swipe_area, ButtonWrapper):
            raise ScriptError
        width = abs(swipe_area.area[0] - swipe_area.area[2])
        high = abs(swipe_area.area[1] - swipe_area.area[3])
        while 1:
            if abs(vector[0] * 2) >= width or abs(vector[1] * 2) >= high:
                break
            vector = (vector[0] * 2, vector[1] * 2)
        self.device.swipe_vector(vector, swipe_area.area, duration=duration)

    def ui_wait_recover(self, interval=1.5):
        """
        Wait anything recover like page or click spark
        """
        self.device.sleep(interval)

    def ui_ensure_index(
            self,
            index,
            check_button,
            prev_button,
            next_button,
            fast=True,
            skip_first_screenshot=False,
            interval=0.3
            ):
        
        logger.hr('UI ensure index')
        check_button = WhiteDigit(check_button)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            current = check_button.ocr_single_line(self.device.image)
            logger.info(f'Current index: {current}')

            diff = index - current
            if diff == 0:
                break
            if current == 0:
                logger.warning(f'ui_ensure_index got an empty current value: {current}')
                break

            button = next_button if diff > 0 else prev_button
            if fast:
                self.device.multi_click(button, abs(diff), interval=interval)
                self.device.sleep(0.2)
            else:
                self.device.click(button)




        


