# name:Gong Xiaoyv
# Time  2024-05-14   3:33
import cv2

from src.Image import Image
from src.Components.Component import Component
import numpy as np

from src.Components.ComponentWidgets.ImageCaculateComponentWidget import ImageCaculateComponentWidget

class ImageCaculateComponent(Component):
    name = 'Image Caculate Component'
    detail = '图像融合模块，实现了图像相加'

    def __init__(self, parent):
        super().__init__(parent)
        self.otherImage = None
        self.controlWidget = ImageCaculateComponentWidget()

        """信号和槽"""
        self.controlWidget.loadImage.connect(self.setOtherImage)

    def processImage(self, image:np.array)->np.ndarray:
        if self.otherImage is None:
            return image
        """针对otherImage和image，进行计算"""
        # 尺寸调整： 将otherImage缩放到和image一样大
        other = cv2.resize(self.otherImage.sourceImage, (image.shape[1], image.shape[0]))
        # 格式调整
        if other.shape[2]==4:
            other = cv2.cvtColor(other, cv2.COLOR_BGRA2BGR)
        if image.shape[2]==4:
            image = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)

        # 进行运算
        processed = np.zeros_like(image)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                processed[i][j] = self.caculatePix(image[i][j], other[i][j])
        return processed

    def setOtherImage(self, otherImage:Image):
        self.otherImage = otherImage
        self.componentAttributeUpdate.emit()

    def caculatePix(self, sourcePix, otherPix):
        """
        子类需要重写该方法，定义像素相加的规则
        """
        return sourcePix