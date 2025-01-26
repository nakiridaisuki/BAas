from module.base.timer import Timer
from module.exception import GameNotRunningError, GameStuckError, RequestHumanTakeover
from module.logger import logger
from tasks.base.ui import UI
from tasks.login.assets.assets_login import *
from tasks.base.page import page_main

class Login(UI):

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
        have_closed_ingame_ads = False
        unknow_timer = Timer(5).start()
        stuck_at_first = True
        stuck_timer = Timer(120).start()

        while 1:
            # Handle unknow condition
            if unknow_timer.reached():
                if not self.device.app_is_running():
                    logger.error('Game died during login')
                    raise GameNotRunningError
                self.ui_touch()
                unknow_timer.reset()
            
            self.device.screenshot()

            # Game always have in-game ads
            if have_closed_ingame_ads:
                if self.ui_page_appear(page_main):
                    break

            # Check if stucked
            if stuck_at_first and stuck_timer.reached():
                logger.error('Game stuck during login')
                raise GameStuckError

            # Need game update in google play
            if self.appear(GOOGLEPLAY_DOWNLOAD):
                logger.error('Need google play update game')
                raise RequestHumanTakeover
                
            # Login
            if self.appear_then_click(NEED_DOWNLOAD, interval=2):
                unknow_timer.reset()
                stuck_at_first = False
                continue
            if self.appear_then_click(TOUCH_TO_START, interval=2):
                unknow_timer.reset()
                stuck_at_first = False
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
