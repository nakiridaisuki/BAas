from module.logger import logger
from module.base.timer import Timer
from module.ocr.ocr import DigitCounter
from module.exception import TaskError
from tasks.base.ui import UI
from tasks.base.page import page_tactical_challenge
from tasks.campaign.assets.assets_campaign_tactical_challenge import *

class TacticalChallenge(UI):
    #TODO may be we need more

    def get_reward(self):
        while 1:
            self.device.screenshot()
            if self.appear(NO_TIME_REWARD, interval=3) and self.appear(NO_DAILY_REWARD, interval=3):
                break

            if self.appear_then_click(TIME_REWARD, interval=2):
                logger.info('Get time reward')
                continue
            elif self.appear_then_click(DAILY_REWARD, interval=2):
                logger.info('Get daily reward')
                continue
            
            if self.ui_reward_acquired(interval=3):
                continue

    def start_challenge(self):
        retry = Timer(5)
        while 1:
            self.device.screenshot()
            if retry.reached():
                retry.reset()
                self.device.click(START_CHALLENGE)
                continue

            if self.appear_then_click(BATTLE_CONFIRM):
                break
            if self.appear_then_click(ATTACK_FORMATION, interval=2):
                retry.reset()
                continue
            if self.appear_then_click(NO_SKIP_BATTLE, interval=2):
                retry.reset()
                continue
            if self.appear_then_click(MOBILIZE, interval=2):
                retry.reset()
                continue

    def check_tickets(self):
        """
        Check current number of tickets
        Return:
            if still have ticket
        """
        ocr = DigitCounter(TC_TICKETS)
        ticket, remain, total = ocr.ocr_single_line(self.device.image)
        if ticket == 0:
            return False
        return True

    def run(self):

        self.ui_ensure(page_tactical_challenge)

        has_ticket = self.check_tickets()
        if not has_ticket:
            self.config.task_delay(server_update=True)
            return
        
        self.get_reward()
        self.start_challenge()
        self.config.task_delay(minute=1.1)

# Test
if __name__ == '__main__':
    test = TacticalChallenge('src')
    test.run()