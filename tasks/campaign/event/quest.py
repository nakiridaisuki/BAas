from module.ocr.ocr import Digit
from module.exception import TaskError, ScriptError
from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_event
from tasks.base.assets.assets_base_page import PAGE_EVENT
from tasks.base.assets.assets_base_ui import ENTER, STARS_3
from tasks.campaign.assets.assets_campaign_share import *
from tasks.campaign.assets.assets_campaign_event_quest import *
from tasks.campaign.assets.assets_campaign_event_share import *
from tasks.campaign.assets.assets_campaign_event_battle import *

class Quest(UI):

    def find_enter_button(self, level:int = None):
        """
        Set the level you want find.
        If not, use the maximum availabal level
        Args:
            level: (int)
            time: (int) how many time you want to sweep
        """

        logger.info('Finding quest enter button')

        if level is not None:
            self.ui_find_level(LEVEL_AREA, SWIPE_AREA, level, STARS_3)
        else:
            level = 999

        self.device.screenshot()
        ocr = Digit(LEVEL_AREA)
        result = ocr.detect_and_ocr(self.device.image)
        for now_level in result[::-1]:
            if int(now_level.ocr_text) > level:
                continue

            x1, y1, x2, y2 = now_level.box
            x2 += 450
            y1 -= 30
            y2 += 50
            ENTER.load_search((x1, y1, x2, y2))
            if ENTER.match_template(self.device.image):
                return now_level
        
        logger.warning("Didn't find enter button")
        raise TaskError

    def switch_quest(self, skip_first_screenshot=False):
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.color_appear_then_click(GOTO_QUEST):
                logger.info('Switch to story page')
                continue
            if self.color_appear(AT_QUEST):
                break

    def battle_pass(self):
        while 1:
            self.device.screenshot()
            if self.appear_then_click(MOBILIZE, interval=2):
                continue
            if self.color_appear_then_click(ACCELERATE_1):
                continue
            if self.color_appear_then_click(ACCELERATE_2):
                continue
            if self.color_appear_then_click(AUTO_MODE):
                continue

            if self.appear(IN_BATTLE, interval=10):
                # May wait more then 60s, need clear stuck record
                self.device.stuck_record_clear()

                logger.info('Waiting for battle end...')
                continue

            if self.appear_then_click(BATTLE_COMPLETE_CONFIRM, interval=2):
                break

    def quest_pass(self):
        finished = False
        started = False
        while 1:
            self.device.screenshot()

            # End
            if finished and self.appear(PAGE_EVENT):
                break

            # Start story
            if not started:
                if self.appear_then_click(QUEST_ENTER, interval=3):
                    continue
            if self.color_appear_then_click(START_MISSION):
                continue

            # Battle pass
            if self.appear_then_click(MOBILIZE, interval=2):
                started = True
                self.battle_pass()
                continue
            if self.appear_then_click(BATTLE_COMPLETE_CONFIRM, interval=2):
                continue
                
            # Handle reward
            if self.appear_then_click(REWARD_SKIP, interval=1):
                continue
            if self.appear_then_click(BATTLE_REWARD_CONFIRM, interval=2):
                finished = True
                continue

    def open_mission_info(self, level, skip_first_screenshot=True):
        self.find_enter_button(level)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.appear(START_MISSION):
                break
            if self.appear_then_click(ENTER, interval=2):
                continue

    def sweep(self, level=None, time=None):
        if level is None:
            logger.warning('Need level')
            raise ScriptError
        
        if time is None:
            logger.warning('Need set sweep time')
            raise ScriptError
        
        self.open_mission_info(level=level)
        self.ui_ensure_index(time, SWEEP_TIME, MINUS_SWEEP_TIME, ADD_SWEEP_TIME)
        timeout = Timer(60).start()
        started = False
        finished = False
        while 1:
            if timeout.reached():
                logger.warning('Sweep faild')
                break
            
            self.device.screenshot()
            if finished and self.color_appear(START_SWEEP, interval=2):
                break
            if self.color_appear_then_click(SWEEP_COMPLETE, interval=2):
                finished = True
                continue
            if self.color_appear_then_click(SWEEP_CONFIRM, interval=2):
                started = True
                continue
            if not started and self.color_appear_then_click(START_SWEEP, interval=2):
                continue

    def auto_clear(self):
        self.ui_ensure(page_event)
        self.switch_quest()

        while 1:
            at_bottom = self.find_enter_button()
            self.quest_pass()
            
            if at_bottom:
                break
            self.ui_wait_recover(3)

    # TODO complete it for scheduler
    def run(self):
        level = 1
        time = 1

        self.sweep(9, 5)



# Test
if __name__ == '__main__':
    test = Quest('src')
    # test.switch_story()
    test.run()