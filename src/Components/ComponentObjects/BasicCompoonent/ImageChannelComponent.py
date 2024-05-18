# name:Gong Xiaoyv
# Time  2024-05-09   9:59
import numpy as np

from src.Components.Component import Component
from src.Components.ComponentWidgets.ImageChannelComponentWidget import ImageChannelComponentWidget


class ImageChannelComponent(Component):
    name = 'RGBChannel Component'
    detail = '调整图片的颜色通道'
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = ImageChannelComponentWidget()
        self.basicControlWidget.setParent(self.controlWidget.ui.enableWidget)

        self.r_val = 255
        self.g_val = 255
        self.b_val = 255
        self.a_val = 255
        """信号和槽"""
        self.controlWidget.ui.R.valChanged.connect(self.setR)
        self.controlWidget.ui.G.valChanged.connect(self.setG)
        self.controlWidget.ui.B.valChanged.connect(self.setB)
        self.controlWidget.ui.A.valChanged.connect(self.setA)



    def processImage(self, image:np.array)->np.ndarray:
        # RGBA 相乘
        src = image
        h, w, channel = src.shape

        print("image shape:",src.shape)
        # 存储处理后图像
        processed = np.zeros_like(image, dtype=np.float32)
        temp = [self.b_val, self.g_val, self.r_val, self.a_val]
        for i in range(channel):
            # 拿出每一个channel的图像
            processed[:, :, i] = image[:, :, i] / 255 * temp[i]
        mapped_image_uint8 = np.round(processed).astype(np.uint8)
        return mapped_image_uint8

    def setR(self, val):
        print(self.r_val, self.g_val, self.b_val, self.a_val)
        self.r_val = val
        self.componentAttributeUpdate.emit()

    def setG(self, val):
        self.g_val = val
        self.componentAttributeUpdate.emit()

    def setB(self, val):
        self.b_val = val
        self.componentAttributeUpdate.emit()

    def setA(self, val):
        self.a_val = val
        self.componentAttributeUpdate.emit()