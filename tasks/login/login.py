from module.base.timer import Timer
from module.base.utils import get_color
from module.exception import GameNotRunningError, GameStuckError, RequestHumanTakeover
from module.logger import logger
from module.ocr.ocr import Ocr
from tasks.base.ui import UI
from tasks.login.assets.assets_login import *
from tasks.base.assets.assets_base_page import PAGE_MAIN, NOW_LOADING

class Login(UI):

    def stuck_at_first(self):
        r, g, b = get_color(self.device.image, TOUCH_TO_START.area)
        if r < 5 and g < 5 and b < 5:
            return True
        return False
    
    def handle_loading(self):
        ocr = Ocr(NOW_LOADING)
        result = ocr.ocr_single_line(self.device.image).lower()
        if 'loading' in result:
            return True
        return False

    def _handle_app_login(self):
        """
        Raises:
            GameNotRunningError
            GameStuckError
        """

        logger.hr('App Login')
        have_closed_ingame_ads = False
        unknow_timer = Timer(5).stop()
        timeout = Timer(180, 30).start()
        app_timer = Timer(20, 5).start()

        while 1:
            self.device.screenshot()

            # Handle unknow condition
            if unknow_timer.reached():
                unknow_timer.reset()
                if not self.device.app_is_running():
                    logger.error('Game died during login')
                    raise GameNotRunningError
                
                if self.handle_loading():
                    continue
                self.ui_touch()
            
            # Game always have in-game ads
            if have_closed_ingame_ads:
                if self.appear(PAGE_MAIN):
                    break

            # Check if stucked
            if app_timer.reached():
                if self.stuck_at_first():
                    logger.error('Game stuck during login')
                    raise GameNotRunningError
                else:
                    app_timer.stop()

            # Need game update in google play
            if self.appear(GOOGLEPLAY_DOWNLOAD):
                logger.error('Need google play update game')
                raise RequestHumanTakeover
                
            # Login
            if self.appear_then_click(NEED_DOWNLOAD, interval=2):
                unknow_timer.reset()
                continue
            if self.appear_then_click(TOUCH_TO_START, interval=2):
                unknow_timer.reset()
                continue

            # Additional
            if self.appear_then_click(GAME_START_ADS, interval=2):
                unknow_timer.reset()
                logger.info('Close game start ad')
                continue
            if self.appear_then_click(DAILY_ATTENDANCE, interval=2):
                unknow_timer.reset()
                logger.info('Get daily attendance reward')
                continue
            if self.appear_then_click(INGAME_ADS, interval=2):
                unknow_timer.reset()
                logger.info('Close in-game ad')
                have_closed_ingame_ads = True
                continue
            

    def handle_app_login(self):
        logger.info('handle_app_login')
        self.device.screenshot_interval_set(1.0)
        self.device.stuck_timer = Timer(300, count=300).start()
        try:
            self._handle_app_login()
        finally:
            self.device.screenshot_interval_set()
            self.device.stuck_timer = Timer(60, count=60).start()

    def app_start(self):
        logger.hr('App start')
        self.device.app_start()
        self.handle_app_login()

    def app_stop(self):
        logger.hr('App stop')
        self.device.app_stop()

    def app_restart(self):
        logger.hr('App restart')
        self.device.app_stop()
        self.device.app_start()
        self.handle_app_login()
        self.config.task_delay(server_update=True)

if __name__ == '__main__':
    test = Login('src')
    test.device.screenshot()
    test.app_restart()
    # test.stuck_at_first()
