# name:Gong Xiaoyv
# Time  2024-05-16   0:22
import cv2
from PyQt6.QtWidgets import QWidget
from src.Components.Component import Component
import numpy as np

class BinarizationComponent(Component):
    name = 'BinarizationComponent'
    detail = '二值化处理图像，使用OTSU方法'
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image: np.array) -> np.ndarray:
        height, width, channels = image.shape
        if channels == 3:
            gray = cv2.cvtColor(image, cv.COLOR_BGR2GRAY)
        elif channels == 4:
            gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        else:
            raise Exception("un valid channel number")
        # 阈值处理，范围0-255， 二进制阈值处理，Otsu阈值法，Ret为阈值，binary为图像
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGRA)
        return binary