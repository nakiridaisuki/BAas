from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_club
from tasks.club.assets.assets_club import *

class Club(UI):

    def run(self):
        self.device.screenshot()
        self.ui_goto(page_club)

        if self.color_appear_then_click(CLUB_ATTENDANCE_CONFIRM):
            logger.info('Get club attendance reward')

if __name__ == '__main__':
    test = Club('src')
    test.run()