from module.base.timer import Timer
from module.logger import logger
from module.exception import ScriptError
from module.ocr.ocr import DigitCounter
from tasks.base.ui import UI
from tasks.base.page import page_lesson, Page
from tasks.lesson.assets.assets_lesson import *

class Lesson(UI):

    for_schale_office = 1
    for_schale_residence_hall = 1
    for_gehenna = 1
    for_abydos = 1
    for_millennium = 1
    for_trinity = 1
    for_red_winter = 1
    for_hyakkiyako = 0
    for_du_shiratori = 0
    for_shanhaijing = 0

    schale_office = Page(SCHALE_OFFICE)
    schale_residence_hall = Page(SCHALE_RESIDENCE_HALL)
    gehenna = Page(GEHENNA)
    abydos = Page(ABYDOS)
    millennium = Page(MILLENNIUM)
    trinity = Page(TRINITY)
    red_winter = Page(RED_WINTER)
    hyakkiyako = Page(HAYKKIYAKO)
    du_shiratori = Page(DU_SHIRATORI)
    shanhaijing = Page(SHANHAIJING)

    schale_office.link(NEXT, schale_residence_hall)
    schale_residence_hall.link(NEXT, gehenna)
    gehenna.link(NEXT, abydos)
    abydos.link(NEXT, millennium)
    millennium.link(NEXT, trinity)
    trinity.link(NEXT, red_winter)
    red_winter.link(NEXT, hyakkiyako)
    hyakkiyako.link(NEXT, du_shiratori)
    du_shiratori.link(NEXT, shanhaijing)
    shanhaijing.link(NEXT, schale_office)

    schale_office.link(PREV, shanhaijing)
    schale_residence_hall.link(PREV, schale_office)
    gehenna.link(PREV, schale_residence_hall)
    abydos.link(PREV, gehenna)
    millennium.link(PREV, abydos)
    trinity.link(PREV, millennium)
    red_winter.link(PREV, trinity)
    hyakkiyako.link(PREV, red_winter)
    du_shiratori.link(PREV, hyakkiyako)
    shanhaijing.link(PREV, du_shiratori)

    page_location = Page(ALL_LOCATIONS)
    page_lesson.link(SELECT_LOCATION, page_location)

    def get_location_button(self, nums=1):
        self.ui_scroll((0, -1), SWIPE_AREA)
        self.ui_wait_recover()

        buttons = []
        for i in range(8, 0, -1):
            if nums <= 0:
                break

            button = globals()['LOCATION_' + str(i)]
            if self.color_appear(button, threshold=10):
                buttons.append(button)
                nums -= 1

        if len(buttons) == 0:
            logger.error("Can't find any button for lesson")
            raise ScriptError
        if nums > 0:
            logger.warning("Can't find enough button for lesson")
        return buttons

    def lesson(self, location: Page = None, time=0):
        if time == 0:
            logger.error('Please set time')
            raise ScriptError

        if location is None:
            logger.error('Need location argument')
            raise ScriptError
        
        logger.hr('Lesson ' + location.name)
        self.ui_goto(location)
        while 1:
            self.device.screenshot()
            if self.color_appear_then_click(ALL_LOCATIONS):
                continue
            if self.appear(LOCATION_LIST):
                break
        
        buttons = self.get_location_button(nums=time)
        for button in buttons:
            retry = Timer(3)
            finished = False
            while 1:
                self.device.screenshot()
                if retry.reached():
                    self.device.click(button)
                    retry.reset()
                    continue
                if self.color_appear_then_click(START_LESSON):
                    retry.stop()
                    continue
                if self.color_appear_then_click(LESSON_CONFIRM):
                    finished = True
                    continue
                if self.color_appear_then_click(RELATIONSHIP_RANKUP):
                    continue
                if finished and self.appear(LOCATION_LIST):
                    break

    def check_tickets(self, times=0, location:str = None):
        """
        Check if the current number of tickets is enough for sweeping
        Args:
            sweep times
        Return:
            min(maximum times can sweep, times),
            raise TaskError if don't have any ticket
        """
        ocr = DigitCounter(LESSON_TICKETS)
        ticket, remain, total = ocr.ocr_single_line(self.device.image)
        if ticket == 0:
            logger.warning("Lesson faild at " + location)
            logger.warning(f"Don't have any tickets")
            times = 0
        elif ticket < times:
            logger.warning("Lesson warning at " + location)
            logger.warning(f"Don't have enough tickets, need {times} but only have {ticket}")
            logger.warning(f"Will only do {ticket} times")
            times = ticket
        return times

    # TODO fix it
    def run(self):

        # Initialize data
        self.for_schale_office = self.config.Lesson_SchaleOffice
        self.for_schale_residence_hall = self.config.Lesson_SchaleResidenceHall
        self.for_gehenna = self.config.Lesson_Gehenna
        self.for_abydos = self.config.Lesson_Abydos
        self.for_millennium = self.config.Lesson_Millennium
        self.for_trinity = self.config.Lesson_Trinity
        self.for_red_winter = self.config.Lesson_Red_winter
        self.for_hyakkiyako = self.config.Lesson_Hyakkiyako
        self.for_du_shiratori = self.config.Lesson_DuShiratori
        self.for_shanhaijing = self.config.Lesson_Shanhaijing

        # Start Lesson
        self.ui_ensure(self.page_location)
        locations = ['schale_office', 'schale_residence_hall', 'gehenna', 'abydos', 'millennium', 'trinity', 'red_winter', 'hyakkiyako', 'du_shiratori', 'shanhaijing']
        for location in locations:
            time = self.__getattribute__('for_' + location)
            page = self.__getattribute__(location)
            
            if time == 0:
                continue
            
            time = self.check_tickets(times=time, location=location)
            if time == 0:
                break
            self.lesson(location=page, time=time)
            self.ui_goto(self.page_location)

        # Delay task
        self.config.task_delay(server_update=True)

if __name__ == '__main__':
    test = Lesson('src')
    # test.device.screenshot()
    # # test.for_millennium = 1
    # buttons = test.get_location_button()
    # print(buttons)
    test.run()
    # print(test.get_location_button(4))