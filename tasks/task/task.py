from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_task
from tasks.task.assets.assets_task import *

class Task(UI):

    def run(self):
        self.device.screenshot()
        self.ui_goto(page_task)

        while 1:
            self.device.screenshot()
            if self.ui_reward_acquired():
                continue
            if self.color_appear_then_click(TASK_CLAIM_ALL):
                logger.info('Claim all')
                continue
            if self.color_appear_then_click(TASK_CLAIM):
                logger.info('Claim daily pyroxenes')
                continue
            if self.color_appear(CLAIMED) and self.color_appear(CLAIMED_ALL):
                logger.info('No tasks need claim')
                break

if __name__ == '__main__':
    test = Task('src')
    test.run()