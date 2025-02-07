from module.exception import TaskError
from module.logger import logger
from module.base.timer import Timer
from tasks.base.ui import UI
from tasks.base.page import page_base_defense, page_item_retrieval, page_commissions
from tasks.base.assets.assets_base_ui import ENTER, STARS_3
from tasks.campaign.assets.assets_campaign_share import *

class Commission(UI):
    for_base_defense = 1
    for_item_retrieval = 1
    AP_needed = 0
    AP_own = 0

    def check_AP(self, times=0, location:str = None):
        """
        Check if current AP are enough for sweeping
        """
        new_times = self.AP_own // self.AP_needed
        if new_times == 0:
            logger.warning("Sweep faild at " + location)
            logger.warning("Don't have any AP for mission")
            raise TaskError
        if new_times < times:
            logger.warning("Sweep faild at " + location)
            logger.warning(f"Don't have enough AP for mission, need {times * self.AP_needed} but only have {self.AP_own}")
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
                self.AP_needed = min((int(now_level.ocr_text)-1) // 2 * 10 + 10, 40)
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
        """
        AP need will chenge with different level
        Porcedure:
            check highest level(open_mission_info)
            -> check if AP is enough(check_AP)
            -> sweep
        """
        self.device.screenshot()
        self.ui_ensure(page_commissions)
        self.AP_own = self.ui_get_AP(skip_first_screenshot=True)

        # Base defense
        if self.for_base_defense > 0:
            self.ui_goto(page_base_defense)
            self.open_mission_info()
            self.for_base_defense = self.check_AP(self.for_base_defense, 'base defense')
            self.sweep(self.for_base_defense)

        # Item retrieval
        if self.for_item_retrieval > 0:
            self.ui_goto(page_item_retrieval)
            self.open_mission_info()
            self.for_item_retrieval = self.check_AP(self.for_item_retrieval, 'item retrieval')
            self.sweep(self.for_item_retrieval)


if __name__ == '__main__':
    test = Commission('src')
    test.for_item_retrieval = 5
    test.for_base_defense = 5
    # test.for_base_defense = 100000
    # test.AP_needed = 40
    # test.AP_own = test.ui_get_AP()
    # print(test.check_AP(test.for_base_defense, 'test'))
    test.run()
        


