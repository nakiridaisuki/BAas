from module.ocr.ocr import Digit
from module.exception import TaskError
from module.logger import logger
from tasks.base.ui import UI
from tasks.base.assets.assets_base_page import PAGE_EVENT
from tasks.base.assets.assets_base_ui import ENTER
from tasks.campaign.assets.assets_campaign_share import START_MISSION
from tasks.campaign.assets.assets_campaign_event_story import *
from tasks.campaign.assets.assets_campaign_event_share import *
from tasks.campaign.assets.assets_campaign_event_battle import *

class Story(UI):

    def find_enter_button(self) -> bool:
        """
        Return:
            if the finded button is at bottom
        """

        logger.info('Finding story enter button')
        self.device.screenshot()
        ocr = Digit(EVENT_LEVEL_AREA)
        result = ocr.detect_and_ocr(self.device.image)
        
        count = 0
        for level in result[::-1]:
            x1, y1, x2, y2 = level.box
            x2 += 450
            y1 -= 20
            y2 += 40
            ENTER.load_search((x1, y1, x2, y2))
            if ENTER.match_template(self.device.image):
                return count == 0
            count += 1
        
        logger.warning("Didn't find enter button")
        raise TaskError

    def switch_story(self, skip_first_screenshot=False):
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.color_appear_then_click(GOTO_STORY):
                logger.info('Switch to story page')
                continue
            if self.color_appear(AT_STORY):
                break

    def battle_pass(self):
        while 1:
            self.device.screenshot()
            if self.appear_then_click(MOBILIZE, interval=2):
                continue
            if self.color_appear_then_click(ACCELERATE_1):
                continue
            if self.color_appear_then_click(ACCELERATE_2):
                continue
            if self.color_appear_then_click(AUTO_MODE):
                continue

            if self.appear(IN_BATTLE, interval=10):
                # May wait more then 60s, need clear stuck record
                self.device.stuck_record_clear()

                logger.info('Waiting for battle end...')
                continue

            if self.appear_then_click(BATTLE_COMPLETE_CONFIRM):
                break

    def story_pass(self):
        finished = False
        started = False
        battle_mode = False
        while 1:
            self.device.screenshot()

            # End
            if finished and self.appear(PAGE_EVENT):
                break

            # Start story
            if not started:
                if self.appear_then_click(ENTER, interval=3):
                    continue
            if self.appear_then_click(STORY_START, interval=2):
                continue
            if self.color_appear_then_click(START_MISSION):
                battle_mode = True
                continue

            # Skip story
            if self.appear_then_click(STORY_MENU, interval=3):
                continue
            if self.appear_then_click(SKIP_STORY, interval=3):
                continue
            if self.appear_then_click(SKIP_CONFIRM, interval=2):
                started = True
                continue

            # Handle battle pass
            if battle_mode:
                if self.appear_then_click(MOBILIZE, interval=2):
                    self.battle_pass()
                    continue
                if self.appear_then_click(BATTLE_COMPLETE_CONFIRM):
                    continue
                
            # Handle reward
            if battle_mode:
                if self.appear_then_click(REWARD_SKIP, interval=1):
                    continue
                if self.appear_then_click(BATTLE_REWARD_CONFIRM, interval=2):
                    finished = True
                    continue
            else:
                if started and self.ui_reward_acquired():
                    finished = True
                    continue

    def auto_story(self):
        self.ui_goto_event()
        self.switch_story()

        while 1:
            at_bottom = self.find_enter_button()
            self.story_pass()
            
            if at_bottom:
                break


# Test
if __name__ == '__main__':
    test = Story('src')
    # test.switch_story()
    test.run()

        


