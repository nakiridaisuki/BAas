from module.ocr.ocr import DigitCounter
from module.exception import TaskError
from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_overpass, page_desert_railroad, page_classroom, page_campaign
from tasks.campaign.assets.assets_campaign_bounty import *
from tasks.campaign.assets.assets_campaign_share import *

class Bounty(UI):
    for_overpass = 2
    for_desert_railrode = 2
    for_classroom = 2

    def check_tickets(self, times=0, location:str = None):
        """
        Check if the current number of tickets is enough for sweeping
        Args:
            sweep times
        Return:
            min(maximum times can sweep, times),
            raise TaskError if don't have any ticket
        """
        BOUNTY_TICKETS.match_color(self.device.image, threshold=30)
        ocr = DigitCounter(BOUNTY_TICKETS)
        ticket, remain, total = ocr.ocr_single_line(self.device.image)
        if ticket == 0:
            logger.warning("Bounty sweep faild at " + location)
            logger.warning(f"Don't have any tickets for mission")
            raise TaskError
        if ticket < times:
            logger.warning("Bounty sweep warning at " + location)
            logger.warning(f"Don't have enough tickets for mission, need {times} but only have {ticket}")
            logger.warning(f"Will only sweep {ticket} times")
            return ticket
        return times

    def find_level(self):
        button: ButtonWrapper = None
        is_current_max = 0
        scrolled = False
        retry = Timer(0.5)
        while 1:
            if retry.reached():
                retry.reset()
                button, is_current_max = self.ui_find_level(area=BOUNTY_LEVEL_AREA)
                if button.name == 'LEVEL_9':
                    break
                if is_current_max:
                    self.ui_scroll((0, -1), SWIPE_AREA)
                    scrolled = True
                    continue
        
        # Wait stage list recover if scrolled
        if scrolled:
            Timer(1.5).start().wait()
        button = self.ui_find_level(area=BOUNTY_LEVEL_AREA)[0]
        return button
    
    def open_mission_info(self, skip_first_screenshot=True):
        button = self.find_level()
        retry = Timer(1)
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.appear(START_MISSION):
                break

            if retry.reached():
                retry.reset()
                self.device.click(button)
                continue
    
    def sweep(self, time):
        self.open_mission_info()
        self.ui_ensure_index(time, SWEEP_TIME, MINUS_SWEEP_TIME, ADD_SWEEP_TIME)
        timeout = Timer(60).start()
        started = False
        finished = False
        while 1:
            if timeout.reached():
                logger.warning('Sweep faild')
                break
            
            self.device.screenshot()
            if finished and self.color_appear(START_SWEEP, interval=2):
                break
            if self.color_appear_then_click(SWEEP_COMPLETE, interval=2):
                finished = True
                continue
            if self.color_appear_then_click(SWEEP_CONFIRM, interval=2):
                started = True
                continue
            if not started and self.color_appear_then_click(START_SWEEP, interval=2):
                continue

    def run(self):
        self.ui_ensure(page_campaign)

        # Overpass
        if self.for_overpass > 0:
            self.ui_goto(page_overpass)
            self.for_overpass = self.check_tickets(self.for_overpass, 'overpass')
            self.sweep(self.for_overpass)

        # Desert_railroad
        if self.for_desert_railrode > 0:
            self.ui_goto(page_desert_railroad)
            self.for_desert_railrode = self.check_tickets(self.for_desert_railrode, 'desert_railrode')
            self.sweep(self.for_desert_railrode)

        # Classroom
        if self.for_classroom > 0:
            self.ui_goto(page_classroom)
            self.for_classroom = self.check_tickets(self.for_classroom, 'classroom')
            self.sweep(self.for_classroom)


# Test
if __name__ == '__main__':
    test = Bounty('src')
    test.for_overpass = 0
    test.for_desert_railrode = 0
    test.run()
    # test.device.screenshot()
    # # test.ui_goto(page_overpass)
    # # test.ui_goto(page_desert_railroad)
    # # test.ui_goto(page_classroom)
    # # test.sweep(1)
    # test.check_tickets(1, 'test')

        


