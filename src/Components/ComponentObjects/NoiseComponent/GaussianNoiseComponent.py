# name:Gong Xiaoyv
# Time  2024-05-15   16:52

import cv2
import numpy as np
from PyQt6.QtGui import QImage
from src.Components.Component import Component

class GaussianNoiseComponent(Component):
    name = 'GaussianNoiseComponent'
    detail = "为图片添加高斯噪声，参数暂时不可调整"
    def __init__(self, parent=None):
        """
        :param image: channel=3 4的np.ndarray
        :return: channel = 4 的np.ndarray
        """
        super().__init__(parent)
        self.controlWidget = self.basicControlWidget

    def processImage(self, image:np.array)->np.ndarray:
        img_height, img_width, img_channels = image.shape
        if img_channels == 3:
            src = image
        elif img_channels == 4:
            src = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        else:
            raise Exception("no vaild image channels")
        img_channels = src.shape[2]

        mean = 0
        # 设置高斯分布的标准差
        sigma = 25
        # 根据均值和标准差生成符合高斯分布的噪声
        gauss = np.random.normal(mean, sigma, (img_height, img_width, img_channels))
        # 给图片添加高斯噪声
        noisy_img = src + gauss
        # 设置图片添加高斯噪声之后的像素值的范围
        noisy_img = np.clip(noisy_img, a_min=0, a_max=255).astype(np.uint8)
        #
        noisy_img = cv2.cvtColor(noisy_img, cv2.COLOR_BGR2BGRA)

        return noisy_img



