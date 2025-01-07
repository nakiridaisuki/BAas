from module.base.timer import Timer
from module.exception import GameNotRunningError, GameStuckError
from module.ocr.ocr import OcrWhiteLetterOnComplexBackground
from module.logger import logger
from tasks.base.ui import UI
from tasks.login.assets.assets_login import *
from tasks.base.page import page_main

class Login(UI):

    def handle_start_ads(self):
        ocr = OcrWhiteLetterOnComplexBackground(GAME_START_ADS)
        result = ocr.ocr_single_line(self.device.image)
        if result == "Don't show again today":
            self.device.click(GAME_START_ADS)
            return True
        return False
    
    def handle_notice(self, interval=0):
        if self.appear_then_click(INGAME_ADS, interval=interval):
            logger.info('Appear in-game notice')
            return True
        return False

    def _handle_app_login(self):
        """
        Raises:
            GameNotRunningError
            GameStuckError
        """

        logger.hr('App Login')
        startup_timer = Timer(20).start()
        have_closed_ingame_ads = False
        app_timer = Timer(5).start()
        stuck_at_first = True
        stuck_timer = Timer(120).start()
        ocr_ad_timer = Timer(5).start()

        while 1:
            # Watch if game alive
            if app_timer.reached():
                if not self.device.app_is_running():
                    logger.error('Game died during login')
                    raise GameNotRunningError
                app_timer.reset()
            
            self.device.screenshot()

            # Game need at least 20s to start
            if startup_timer.reached() and have_closed_ingame_ads:
                if self.ui_page_appear(page_main):
                    break

            # Check if stuck at initial black page
            if stuck_at_first and stuck_timer.reached():
                if not self.appear(STUCK_AT_FIRST):
                    stuck_at_first = False
                    continue
                if stuck_timer.reached():
                    logger.error('Game stuck during login')
                    raise GameStuckError
                continue
                
            # Login
            if self.appear_then_click(NEED_DOWNLOAD, interval=2):
                continue
            if self.appear_then_click(TOUCH_TO_START, interval=2):
                continue

            # Additional
            if ocr_ad_timer.reached():
                if self.handle_start_ads():
                    continue
                ocr_ad_timer.reset()
            if self.appear_then_click(ARONA_PAD, interval=2):
                continue
            if self.handle_notice(interval=2):
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
