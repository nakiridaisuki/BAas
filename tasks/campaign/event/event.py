from module.ocr.ocr import Digit
from module.exception import TaskError, ScriptError
from module.logger import logger
from module.base.timer import Timer
from tasks.base.page import page_campaign
from tasks.base.assets.assets_base_page import CAMPAIGN_GOTO_EVENT
from tasks.base.assets.assets_base_page import PAGE_EVENT
from tasks.campaign.event.story import Story
from tasks.campaign.event.quest import Quest
from tasks.campaign.assets.assets_campaign_event_story import STORY_MENU
from tasks.campaign.assets.assets_campaign_event_share import *
from tasks.campaign.assets.assets_campaign_event_battle import *

class Event(Story, Quest):

    # TODO complete it for scheduler
    def run(self):
        self.ui_ensure(page_campaign)
        retry = Timer(1)
        while 1:
            self.device.screenshot()
            if retry.reached():
                retry.reset()
                logger.info(f'Page switch: page_campaign -> page_event')
                self.device.click(CAMPAIGN_GOTO_EVENT)
                continue
            if self.appear(PAGE_EVENT):
                logger.info(f'Page arrive: page_event')
                break
            if self.appear(STORY_MENU):
                logger.info('New event detected')
                logger.info('Will start auto pass story and quest')
                with self.config.multi_set():
                    self.config.EventStory_State = True
                    self.config.EventQuest_State = True
                break

        if self.config.EventStory_AutoPass and self.config.EventStory_State:
            self.auto_story()
            self.config.EventStory_State = False

        if self.config.EventQuest_AutoPass and self.config.EventQuest_State:
            self.auto_quest()
            self.config.EventQuest_State = False

        self.switch_quest()
        level = self.config.EventQuest_Area
        time = self.config.EventQuest_Time
        self.sweep(level, time)

        self.config.task_delay(server_update=True)

# Test
if __name__ == '__main__':
    test = Event('src')
    # test.switch_story()
    test.run()