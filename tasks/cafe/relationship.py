import numpy as np
import cv2
from module.logger import logger
from tasks.base.ui import UI
from tasks.base.page import page_cafe
from tasks.base.assets.assets_base_page import NOW_LOADING
from tasks.lesson.assets.assets_lesson import RELATIONSHIP_RANKUP
from tasks.cafe.assets.assets_cafe_invite import MOVE_CAFE, GOTO_CAFE_1, GOTO_CAFE_2
from tasks.cafe.assets.assets_cafe_relationship import *

class Relationship(UI):

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
                    self.device.click(EDIT, control_check=False)
                    continue
            
            if self.color_appear_then_click(RELATIONSHIP_RANKUP):
                continue
            if self.appear(FINISH_EDIT, interval=2):
                self.device.click(FINISH_EDIT, control_check=False)
                reflashed = True
                continue

    def relationship(self):
        RELATIONSHIP_HINT.load_search((0, 0, 1280, 720))

        retry = 0
        no_click_count = 0
        while 1:
            logger.info(f'Relationship retry {retry + 1} time')
            self.device.screenshot()


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
            if clicked:
                no_click_count = 0
            else:
                no_click_count += 1

            if no_click_count > 1:
                break
            if retry >= 5:
                break
                
            self.reflash()

    def run(self):
        self.ui_ensure(page_cafe)

        self.relationship()
        self.switch_cafe()
        self.relationship()

        self.config.task_delay(180)