from module.ocr.ocr import Digit
from module.base.timer import Timer
from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_cafe
from tasks.cafe.assets.assets_cafe_earning import *

class Earning(UI):

    def reward(self):
        logger.info('Get cafe earning')
        ocr = Digit(CAFE_EARNING)
        ocr_timer = Timer(2)
        while 1:
            self.device.screenshot()

            if self.ui_reward_acquired(interval=5):
                break

            if self.color_appear_then_click(EARNING_CLAIM, interval=2):
                continue

            if ocr_timer.reached():
                ocr_timer.reset()
                result = ocr.ocr_single_line(self.device.image)
                if result > 10:
                    self.device.click(CAFE_EARNING)
                    continue
                else:
                    logger.info('Cafe earning less then 10%')
                    break

    def run(self):
        self.ui_ensure(page_cafe)

        self.reward()
        self.config.task_delay(server_update=True)
            