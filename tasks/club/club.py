from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_club, page_main
from tasks.club.assets.assets_club import *

class Club(UI):

    def run(self):
        """
        Page:
            in: any
            out: page_main
        """
        self.ui_ensure(page_club)

        timeout = Timer(10).start()
        clicked = False
        while 1:
            self.device.screenshot()
            if timeout.reached():
                break
            if self.color_appear_then_click(CLUB_ATTENDANCE_CONFIRM, interval=1):
                logger.info('Get club attendance reward')
                clicked = True
                continue
            # I have no idea how to do it without not, so that me use it
            if clicked and not self.color_appear(CLUB_ATTENDANCE_CONFIRM):
                break
        
        if not clicked:
            logger.error("Didn't get club attendance reward")
        self.config.task_delay(server_update=True)


if __name__ == '__main__':
    test = Club('src')
    test.run()