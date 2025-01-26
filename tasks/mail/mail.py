from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_mail
from tasks.mail.assets.assets_mail import *

class Mail(UI):
    def run(self):
        self.ui_ensure(page_mail, skip_first_screenshot=False)
        while 1:
            self.device.screenshot()
            if self.color_appear_then_click(MAIL_CLAIM):
                logger.info("Claim mail")
                continue
            if self.color_appear(NO_MAIL):
                break
            
if __name__ == '__main__':
    test = Mail('src')
    test.run()