from module.logger import logger
from module.exception import ScriptError
from tasks.base.ui import UI
from tasks.base.page import page_cafe
from tasks.base.assets.assets_base_page import NOW_LOADING
from tasks.cafe.assets.assets_cafe_invite import *
from tasks.cafe.assets.assets_cafe_charater import *

class Invite(UI):

    name_cafe1 = 'yuuka'
    name_cafe2 = 'serika'

    def find_student(self, name:str = None):
        """
        Find the invite button of student in invite list
        INVITE_BUTTON.search will be chenged after calling this function
        so you can use functhons like self.appear(INVITE_BUTTON) directly

        Return:
            True if success
        """
        if name is None:
            logger.error("Don't set name")
            raise ScriptError
        
        button:ButtonWrapper = globals()['INVITE_' + name.upper()]
        button.load_search(STUDENT_AREA.search)

        #TODO add list button check

        for _ in range(30):
            self.device.screenshot()
            if button.match_template(self.device.image, similarity=0.7):
                x1, y1, x2, y2 = button.button
                y1 -= 20
                x2 += 380
                y2 += 20

                INVITE_BUTTON.load_search((x1, y1, x2, y2))
                return True

            self.ui_scroll((0, -1), INVITE_SWIPE_AREA)
            self.device.click_record_clear()
            self.device.sleep(0.6)
        return False

    def name_process(self, name:str):
        name = name.replace(' (', ' ').replace(')', ' ').replace(' ', '_').lower()
        return name
    
    def invite(self, name:str):
        """
        Args:
            name: (str) student's name
        """
        logger.hr(f'Invite student {name}')

        # Open invite list
        while 1:
            self.device.screenshot()
            if self.appear(CANNOT_INVITE):
                logger.warning("Can't invite student now")
                return
            if self.appear_then_click(INVITATION):
                continue
            if self.appear(INVITE_LIST):
                break

        logger.info("Find student")
        success = self.find_student(name=self.name_process(name))
        if not success:
            logger.warning(f"Can't find student {name}")
            logger.info('Choose random student')
            x1, y1, x2, y2 = INVITE_SWIPE_AREA.area
            x2 += 150
            INVITE_BUTTON.load_search((x1, y1, x2, y2))

        # Invite
        while 1:
            self.device.screenshot()
            if self.appear_then_click(INVITE_BUTTON):
                continue
            if self.color_appear_then_click(INVITE_CONFIRM):
                continue
            if self.appear(INVITE_COMPLETE):
                break

    def switch_cafe(self):
        while 1:
            self.device.screenshot()
            if self.appear_then_click(MOVE_CAFE):
                continue
            if self.appear_then_click(GOTO_CAFE_1):
                continue
            if self.appear_then_click(GOTO_CAFE_2):
                continue
            if self.appear(NOW_LOADING):
                break


    def run(self):
        self.ui_ensure(page_cafe)

        self.invite(self.name_cafe1)
        self.switch_cafe()
        self.invite(self.name_cafe2)

        if self.config.Invite_Interval == '20':
            self.config.task_delay(60 * 20)
        else:
            self.config.task_delay(server_update=True)