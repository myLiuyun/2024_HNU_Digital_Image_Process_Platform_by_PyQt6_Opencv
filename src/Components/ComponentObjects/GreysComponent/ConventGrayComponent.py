# name:Gong Xiaoyv
# Time  2024-05-13   17:48
import cv2
from PyQt6.QtWidgets import QWidget
from src.Components.Component import Component
import numpy as np

class ConventGrayComponent(Component):
    name = 'Convent Gray Component'
    detail = "将图像转化为灰度图进行显示"
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image:np.array)->np.ndarray:
        """
        将图像转为灰度图显示
        """
        processed_image = image
        if image.shape[2]==3:
            processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        elif image.shape[2]==4:
            processed_image = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        processed_image = cv2.cvtColor(processed_image, cv2.COLOR_GRAY2BGRA)
        return processed_image