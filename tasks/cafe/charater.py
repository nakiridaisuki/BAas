from module.logger import logger
from module.exception import ScriptError
from tasks.base.ui import UI
from tasks.cafe.assets.assets_cafe_charater import *
from tasks.cafe.assets.assets_cafe_invite import STUDENT_AREA, INVITE_SWIPE_AREA, INVITE_BUTTON

from module.base.utils import crop

class Charater(UI):

    def find_student(self, name:str = None):
        """
        Find the invite button of student in invite list
        INVITE_BUTTON.search will be chenged after calling this function
        so you can use functhons like self.appear(INVITE_BUTTON) directly
        """
        if name is None:
            logger.error("Don't set name")
            raise ScriptError
        
        button:ButtonWrapper = globals()['INVITE_' + name.upper()]
        button.load_search(STUDENT_AREA.search)

        #TODO add list button check

        for _ in range(40):
            self.device.screenshot()
            if button.match_template(self.device.image, similarity=0.7):
                x1, y1, x2, y2 = button.button
                y1 -= 20
                x2 += 380
                y2 += 20

                INVITE_BUTTON.load_search((x1, y1, x2, y2))
                break

            self.ui_scroll((0, -1), INVITE_SWIPE_AREA)
            self.device.click_record_clear()
            self.device.sleep(0.6)


if __name__ == '__main__':
    test = Charater('src')
    test.find_student('hoshino')
    print(INVITE_BUTTON.button)