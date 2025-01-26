from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_club
from tasks.club.assets.assets_club import *

class Club(UI):

    def run(self):
        self.device.screenshot()
        self.ui_ensure(page_club)

        timeout = Timer(10).start()
        while not timeout.reached():
            if self.color_appear_then_click(CLUB_ATTENDANCE_CONFIRM, interval=2):
                logger.info('Get club attendance reward')
                return
        logger.error("Didn't get club attendance reward")


if __name__ == '__main__':
    test = Club('src')
    test.run()