# name:Gong Xiaoyv
# Time  2024-05-06   17:49

import cv2
import numpy as np
from PyQt6.QtGui import QImage, QPixmap
import src.Components
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtCore import QObject

class Image(QObject):
    imageComponentUpdadte = pyqtSignal()

    def __init__(self, img_path:str=None, img_type:str=None, source_img:np.ndarray=None, parent=None):
        super(Image, self).__init__(parent)
        if img_path is not None:
            self.sourceImage = cv2.imread(img_path,flags=cv2.IMREAD_UNCHANGED)
        elif source_img is not None:
            self.sourceImage = source_img
        self.effects = list()  # 施加到这个Image上的效果

    def getProcessedImage(self):
        ans = self.sourceImage
        for component in self.effects:
            if component.enable:
                ans = component.processImage(ans)
        return ans
    def getSourceImagePixmap(self)->QPixmap:
        """
        转换到QPixmap，并返回
        :return:
        """
        return self.ndarrayToQPixmap(self.sourceImage)

    def getProcesedImagePixmap(self)->QPixmap:
        """
        得到转换后的图像的Pixmap格式
        :return:
        """
        ans = self.sourceImage
        for component in self.effects:
            if component.enable:
                ans = component.processImage(ans)
        # self.showImage(ans)
        return self.ndarrayToQPixmap(ans)

    def ndarrayToQPixmap(self, cv_image:np.ndarray) -> QPixmap:
        # 如果返回灰度图，转为RGBA的四通道，具有第三维
        if len(cv_image.shape) == 2:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_GRAY2BGRA)
        height, width, channel = cv_image.shape
        bytes_per_line = channel * width
        # 根据channel数，转为QImage
        if channel == 4:  # Check if the image is RGBA
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGRA2RGBA)
            qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888)
            qimage.save("./img.png")
        else:
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2RGB)
            qimage = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format.Format_RGB888)
        return QPixmap.fromImage(qimage)

    def addComponent(self, component:src.Components):
        print(f"add component:{component.getName()}")
        self.effects.append(component)
        """连接Signal，监听Component的信号改变"""
        component.componentAttributeUpdate.connect(self.imageComponentUpdadte)

    def isNull(self):
        return self.sourceImage is None

    def showImage(self, image):
        cv2.imshow("image", image)  # 显示图片，后面会讲解
        cv2.waitKey(0)  # 等待按键