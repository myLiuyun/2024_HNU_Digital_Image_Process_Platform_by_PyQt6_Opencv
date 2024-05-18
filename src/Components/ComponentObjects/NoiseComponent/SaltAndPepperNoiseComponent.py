# name:Gong Xiaoyv
# Time  2024-05-15   17:16
import cv2
import numpy as np
from PyQt6.QtGui import QImage
from src.Components.Component import Component
from src.Components.ComponentWidgets.SaltAndPepperNoiseComponentWidget import SaltAndPepperNoiseComponentWidget

class SaltAndPepperNoiseComponent(Component):
    name = 'SaltAndPepperNoiseComponent'
    detail = "椒盐噪声，可选择添加盐噪声还是胡椒噪声"
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = SaltAndPepperNoiseComponentWidget()
        self.slat = True
        self.pepper = True
        self.amount = 0.01 # 噪声的像素比例
        """信号和槽"""
        self.controlWidget.ui.enable.toggled.connect(self.setEnabel)
        self.controlWidget.ui.salt.toggled.connect(self.setSalt)
        self.controlWidget.ui.pepper.toggled.connect(self.setPepper)

    def processImage(self, image: np.array) -> np.ndarray:
        """
        :param image: channel=3 4的np.ndarray
        :return: channel = 4 的np.ndarray
        """
        img_height, img_width, img_channels = image.shape
        if img_channels == 3:
            noisy_img = image
        elif img_channels == 4:
            noisy_img = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        else:
            raise Exception("no vaild image channels")

        # 添加salt噪声
        if self.slat:
            num_salt = np.ceil(self.amount * image.size)
            # 设置添加噪声的坐标位置
            coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
            noisy_img[coords[0], coords[1], :] = [255, 255, 255]
        if self.pepper:
        # 添加pepper噪声
            num_pepper = np.ceil(self.amount * image.size)
            # 设置添加噪声的坐标位置
            coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
            noisy_img[coords[0], coords[1], :] = [0, 0, 0]

        noisy_img = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2BGRA)
        return noisy_img

    def setSalt(self, b):
        self.slat = b
        self.componentAttributeUpdate.emit()

    def setPepper(self, b):
        self.pepper = b
        self.componentAttributeUpdate.emit()
