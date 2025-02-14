from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_task
from tasks.task.assets.assets_task import *

class Task(UI):

    def claim(self):
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
                break

    def run(self):

        self.ui_ensure(page_task)
        self.claim()
        self.config.task_delay(server_update=True)


if __name__ == '__main__':
    test = Task('src')
    test.run()