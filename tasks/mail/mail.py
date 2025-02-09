from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_mail, page_main
from tasks.mail.assets.assets_mail import *

class Mail(UI):

    retry_delay = 3

    def claim(self):
        """
        Return:
            if can claim all thing will return True
        """
        while 1:
            self.device.screenshot()
            if self.color_appear_then_click(MAIL_CLAIM):
                logger.info("Claim mail")
                continue
            if self.color_appear_then_click(MAIL_NOTICE):
                logger.info(f"Can't claim all things now, will retry in {self.retry_delay} minutes")
                return False
            if self.color_appear(NO_MAIL):
                return True

    def run(self):
        """
        Page:
            in: any
            out: page_main
        """
        self.ui_ensure(page_mail)
        success = self.claim()
        if success:
            self.config.task_delay(minute=self.retry_delay)
        else:
            self.config.task_delay(server_update=True)
        self.ui_goto(page_main)
            
if __name__ == '__main__':
    test = Mail('src')
    test.run()