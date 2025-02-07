from module.ocr.ocr import DigitCounter, Digit
from module.exception import TaskError
from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_overpass, page_desert_railroad, page_classroom, page_campaign
from tasks.base.assets.assets_base_ui import ENTER, STARS_3
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
        """
        Find maximum level that have 3 star for sweeping
        You need call it before use button ENTER
        """

        result = self.ui_find_level(LEVEL_AREA, SWIPE_AREA, check=STARS_3)
        for now_level in result[::-1]:
            x1, y1, x2, y2 = now_level.box
            x2 += 450
            y1 -= 30
            y2 += 50
            ENTER.load_search((x1, y1, x2, y2))
            if ENTER.match_template(self.device.image):
                return
        
    
    def open_mission_info(self, skip_first_screenshot=True):
        self.find_level()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.appear(START_MISSION):
                break
            if self.appear_then_click(ENTER, interval=2):
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
    test.for_classroom = 1
    test.run()
    # test.device.screenshot()
    # # test.ui_goto(page_overpass)
    # # test.ui_goto(page_desert_railroad)
    # # test.ui_goto(page_classroom)
    # # test.sweep(1)
    # test.check_tickets(1, 'test')

        


