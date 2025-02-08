from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_mail
from tasks.mail.assets.assets_mail import *

class Mail(UI):

    def claim(self):
        clicked = False
        while 1:
            self.device.screenshot()
            if self.color_appear_then_click(MAIL_CLAIM):
                logger.info("Claim mail")
                clicked = True
                continue
            if self.color_appear(NO_MAIL):
                break
        return clicked

    def run(self):
        self.ui_ensure(page_mail)
        success = self.claim()
        if success:
            self.config.task_delay(minute=3)
        else:
            self.config.task_delay(server_update=True)
            
if __name__ == '__main__':
    test = Mail('src')
    test.run()