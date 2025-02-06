import numpy as np
import cv2
from module.ocr.ocr import Digit
from module.base.timer import Timer
from module.logger import logger
from tasks.cafe.charater import Charater
from tasks.base.page import page_cafe
from tasks.base.assets.assets_base_page import NOW_LOADING
from tasks.lesson.assets.assets_lesson import RELATIONSHIP_RANKUP
from tasks.cafe.assets.assets_cafe import *
from tasks.cafe.assets.assets_cafe_invite import *

class Cafe(Charater):

    name_cafe1 = 'yuuka'
    name_cafe2 = 'serika'

    def invite(self, name:str):
        """
        Args:
            name: (str) student's name
        """
        self.ui_ensure(page_cafe)

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
        
        self.find_student(name=name)

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
    
    def relationship_hint_extract(self, image):
        lower = np.array([150, 150, 0])
        upper = np.array([255, 255, 20])
        mask = cv2.inRange(image, lower, upper)
        return cv2.bitwise_and(image, image, mask=mask)
    
    def delet_area(self, image, area):
        x1, y1, x2, y2 = area
        image[y1-5:y2+5, x1-5:x2+5] = [0, 0, 0]
        return image
    
    def reflash(self):
        reflashed = False
        while 1:
            self.device.screenshot()
            if self.appear(EDIT, interval=2):
                if reflashed:
                    break
                else:
                    self.device.click(EDIT)
                    continue
            
            if self.color_appear_then_click(RELATIONSHIP_RANKUP):
                continue
            if self.appear_then_click(FINISH_EDIT, interval=2):
                reflashed = True
                continue



    def relationship(self):
        RELATIONSHIP_HINT.load_search((0, 0, 1280, 720))

        retry = 0
        no_click_count = 0
        while 1:
            logger.info(f'Relationship retry {retry + 1} time')
            self.device.screenshot()

            if no_click_count > 1:
                break

            img = self.relationship_hint_extract(self.device.image)
            clicked = False
            while 1:
                if RELATIONSHIP_HINT.match_template(img, similarity=0.7):
                    img = self.delet_area(img, RELATIONSHIP_HINT.button)
                    x, y = RELATIONSHIP_HINT.buttons[0]._button_offset
                    x += 40
                    y += 10
                    RELATIONSHIP_HINT.buttons[0]._button_offset = (x, y)
                    self.device.click(RELATIONSHIP_HINT, control_check=False)
                    self.device.sleep(0.5)
                    clicked = True
                else:
                    break
            
            retry += 1
            self.reflash()
            if clicked:
                no_click_count = 0
            else:
                no_click_count += 1
                


    def invite_then_relationship(self):
        self.invite(self.name_cafe1)
        self.relationship()

        self.switch_cafe()

        self.invite(self.name_cafe2)
        self.relationship()

    def reward(self):
        self.ui_ensure(page_cafe)

        ocr = Digit(CAFE_EARNING)
        ocr_timer = Timer(2)
        while 1:
            self.device.screenshot()

            if self.ui_reward_acquired(interval=5):
                break

            if self.color_appear_then_click(EARNING_CLAIM, interval=2):
                continue

            if ocr_timer.reached():
                ocr_timer.reset()
                result = ocr.ocr_single_line(self.device.image)
                if result > 10:
                    self.device.click(CAFE_EARNING)
                    continue
                else:
                    logger.info('Cafe earning less then 10%')
                    break

    def run(self):
        self.device.screenshot()
        logger.info('Get cafe earning')
        self.reward()

if __name__ == '__main__':
    test = Cafe('src')
    # test.invite('hoshino')
    # test.color_appear(INVITE_CONFIRM)
    test.device.screenshot()
    # test.invite_then_relationship()
    # test.relationship()
    test.invite('hoshino')