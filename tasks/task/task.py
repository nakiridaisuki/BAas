from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_task
from tasks.task.assets.assets_task import *

class Task(UI):

    def claim(self):
        clicked = False
        while 1:
            self.device.screenshot()
            if self.ui_reward_acquired():
                continue
            if self.color_appear_then_click(TASK_CLAIM_ALL):
                clicked = True
                logger.info('Claim all')
                continue
            if self.color_appear_then_click(TASK_CLAIM):
                clicked = True
                logger.info('Claim daily pyroxenes')
                continue
            if self.color_appear(CLAIMED) and self.color_appear(CLAIMED_ALL):
                break
        return clicked

    def run(self):

        self.ui_ensure(page_task)
        success =  self.claim()

        if success:
            self.config.task_delay(minute=5)
        # TODO this need to update at 17:00 every day, try to figure out how to use datetime
        elif self.config.Task_NewDay is True:
            self.config.task_delay(minute=720)
            self.config.Task_NewDay = False
        else:
            self.config.task_delay(server_update=True)
            self.config.Task_NewDay = True

if __name__ == '__main__':
    test = Task('src')
    test.run()