from module.ocr.ocr import DigitCounter
from module.exception import TaskError
from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_trinity, page_gehenna, page_millennium, page_campaign
from tasks.base.assets.assets_base_ui import ENTER, STARS_3
from tasks.campaign.assets.assets_campaign_scrimmage import *
from tasks.campaign.assets.assets_campaign_share import *

class Scrimmage(UI):
    for_trinity = 2
    for_gehenna = 2
    for_millennium = 2
    AP_needed = 10
    AP_own = 0

    def check_tickets(self, times=0, location:str = None):
        """
        Check if the current number of tickets is enough for sweeping
        Args:
            sweep times
        Return:
            min(maximum times can sweep, times),
            raise TaskError if don't have any ticket
        """
        # Reuse the button of bounty because they are in the same position
        SCRIMMAGE_TICKET.match_color(self.device.image, threshold=30)
        ocr = DigitCounter(SCRIMMAGE_TICKET)
        ticket, remain, total = ocr.ocr_single_line(self.device.image)
        AP_times = self.AP_own // self.AP_needed
        new_times = min(ticket, AP_times)
        if new_times == 0:
            logger.warning("Scrimmage sweep faild at " + location)
            logger.warning(f"Don't have any tickets for mission")
            raise TaskError
        if new_times < times:
            logger.warning("Scrimmage sweep warning at " + location)
            logger.warning("Don't have enough tickets or AP for mission")
            logger.warning(f"need {times} tickets but only have {ticket}")
            logger.warning(f"need {self.AP_needed} tickets but only have {self.AP_own}")
            logger.warning(f"Will only sweep {new_times} times")
            return new_times
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
                if int(now_level.ocr_text) > 1:
                    self.AP_needed = 15
                return
    
    def open_mission_info(self, skip_first_screenshot=True):
        self.find_level()
        while 1:
            if skip_first_screenshot:
                skip_first_screenshot = False
            else:
                self.device.screenshot()

            if self.color_appear(START_MISSION):
                break
            if self.appear_then_click(ENTER, interval=2):
                continue
    
    def sweep(self, time):
        self.AP_own -= self.AP_needed * time
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
        self.AP_own = self.ui_get_AP(skip_first_screenshot=True)

        # Trinity
        if self.for_trinity > 0:
            self.ui_goto(page_trinity)
            self.for_trinity = self.check_tickets(self.for_trinity, 'trinity')
            self.open_mission_info()
            self.sweep(self.for_trinity)

        # Gehenna
        if self.for_gehenna > 0:
            self.ui_goto(page_gehenna)
            self.for_gehenna = self.check_tickets(self.for_gehenna, 'gehenna')
            self.open_mission_info()
            self.sweep(self.for_gehenna)

        # Trinity
        if self.for_trinity > 0:
            self.ui_goto(page_millennium)
            self.for_millennium = self.check_tickets(self.for_millennium, 'millennium')
            self.open_mission_info()
            self.sweep(self.for_millennium)


# Test
if __name__ == '__main__':
    test = Scrimmage('src')
    # test.run()
    result = test.ui_find_level(LEVEL_AREA, SWIPE_AREA, check=STARS_3)
    print(result)

    # test.device.screenshot()
    # test.ui_goto(page_trinity)
    # test.ui_goto(page_gehenna)
    # test.ui_goto(page_millennium)
    # test.AP_own = test.ui_get_AP()
    # test.check_tickets(6, 'test')
    # test.open_mission_info()
    # test.sweep(1)


        


