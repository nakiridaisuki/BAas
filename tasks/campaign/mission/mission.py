from module.logger import logger
from module.exception import ScriptError, TaskError
from module.base.timer import Timer
from module.ocr.ocr import Ocr
from module.base.utils import *
from tasks.base.ui import UI
from tasks.campaign.assets.assets_campaign_mission import *
from tasks.campaign.assets.assets_campaign_share import *
from tasks.base.assets.assets_base_ui import ENTER, STARS_3
from tasks.base.page import page_mission

# TODO add auto push mission

class Mission(UI):
    max_area_number = 24

    def set_mission_area(self, index=0):
        if self.ui_get_current_page() != page_mission:
            self.ui_goto(page_mission)
        if index <= 0 or index > self.max_area_number:
            logger.error(f'Please set a valid area number, current area number is {index}')
            logger.error(f'Supported area number: 1~{self.max_area_number}')
            raise ScriptError
        self.ui_ensure_index(index, MISSION_AREA, PREV_MISSION, NEXT_MISSION)

    def goto_hard(self, interval=2):
        retry = Timer(interval)
        while 1:
            self.device.screenshot()
            if self.color_appear(HARD):
                break
            if retry.reached():
                retry.reset()
                self.device.click(HARD)

    def goto_normal(self, interval=2):
        retry = Timer(interval)
        while 1:
            self.device.screenshot()
            if self.color_appear(NORMAL):
                break
            if retry.reached():
                retry.reset()
                self.device.click(NORMAL)

    def find_level(self, level='1-1', mode='normal'):
        """
        Arg:
            level: (str) A mission id like 3-4, 18-4
            mode: (str) normal or hard
        """
        area, id = int(level.split('-')[0]), int(level.split('-')[1])
        self.set_mission_area(area)

        if not mode == 'normal' and not mode == 'hard':
            logger.error(f'Get error argument {mode}')
            raise ScriptError

        if mode == 'normal':
            if id <= 2:
                self.ui_scroll((0, 1), SWIPE_AREA)
                self.ui_scroll((0, 1), SWIPE_AREA)
            else:
                self.ui_scroll((0, -1), SWIPE_AREA)
                self.ui_scroll((0, -1), SWIPE_AREA)
            self.ui_wait_recover()

        ocr = Ocr(MISSION_LEVEL_AREA)
        self.device.screenshot()
        result = ocr.detect_and_ocr(self.device.image)

        matched = False
        for now_level in result:
            if now_level.ocr_text == level:
                x1, y1, x2, y2 = now_level.box
                m = (x1 + x2) // 2
                STARS_3.load_search((m-30, y1, m+30, y2+30))
                ENTER.load_search((x1, y1-20, x2+450, y2+40))
                if STARS_3.match_template(self.device.image, similarity=0.7):
                    matched = True

                break

        if not matched:
            logger.warning("Can't find mission " + level)
            logger.warning("Please check if it has three stars")
            raise TaskError
    
    def check_AP(self, times=0, location:str = None, ap=0):
        """
        Check if current AP are enough for sweeping
        """
        new_times = ap // 10
        if 'hard' in location:
            new_times = ap // 20
        if new_times == 0:
            logger.warning("Sweep faild at " + location)
            logger.warning("Don't have any AP for mission")
            raise TaskError
        if new_times < times:
            logger.warning("Sweep faild at " + location)
            logger.warning(f"Don't have enough AP for mission, need {times * 10} but only have {ap}")
            logger.warning(f"Will only sweep {new_times} times")
            return new_times
        return times
    
    def mission(self, mode='normal', level='1-1', times=1):
        self.ui_ensure(page_mission)

        ap = self.ui_get_AP()
        times = self.check_AP(times, mode+level, ap)

        if mode == 'normal':
            self.goto_normal()
        elif mode == 'hard':
            self.goto_hard()
        else:
            logger.error('Unknow mission mode' + mode)
            raise ScriptError
        
        self.find_level(level=level, mode=mode)

        retry = Timer(2)
        started = False
        finished = False
        while 1:
            self.device.screenshot()
            if finished and self.color_appear(MISSION_START_SWEEP):
                break
            if self.color_appear_then_click(SWEEP_COMPLETE, interval=2):
                finished = True
                continue
            if self.color_appear_then_click(SWEEP_CONFIRM, interval=2):
                started = True
                continue

            if started:
                continue

            if self.color_appear(MISSION_START_SWEEP, interval=3):
                self.ui_ensure_index(times, MISSION_SWEEP_TIME, MISSION_SWEEP_MINUS, MISSION_SWEEP_ADD)
                self.interval_reset(MISSION_START_SWEEP, interval=3)
                self.device.click(MISSION_START_SWEEP)
                retry.reset()
                continue
            if self.appear_then_click(ENTER, interval=2):
                continue

    def hard(self):
        area = self.config.HardMission_Area
        time = self.config.HardMission_Time

        self.mission('hard', area, time)
        self.config.task_delay(server_update=True)

    def normal(self):
        area = self.config.NormalMission_Area
        time = self.config.NormalMission_Time

        self.mission('normal', area, time)
        self.config.task_delay(server_update=True)


if __name__ == '__main__':
    test = Mission('src')
    test.device.screenshot()
    # test.mission(mode='normal', level='20-4', times=20)
    test.mission(mode='hard', level='20-3', times=3)
