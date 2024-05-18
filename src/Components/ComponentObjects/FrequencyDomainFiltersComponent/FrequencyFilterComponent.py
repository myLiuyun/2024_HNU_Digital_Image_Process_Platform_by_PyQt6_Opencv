# name:Gong Xiaoyv
# Time  2024-05-14   1:28
import cv2

from src.Components.Component import Component
from src.Components.ComponentWidgets.FrequencyDomainFilterComponentWidget import FrequencyDomainFilterComponentWidget
import numpy as np

class FrequencyFilterComponent(Component):
    """
    频域滤波器的基类，增加两个方法，实现频率图和RGBA彩色图的转换
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = FrequencyDomainFilterComponentWidget()
        self.filterType = 'High'
        """信号和槽"""
        self.controlWidget.ui.enableButton.toggled.connect(self.setEnabel)
        self.controlWidget.ui.high.toggled.connect(self.setHighFilter)
        self.controlWidget.ui.low.toggled.connect(self.setLowFilter)


    def processImage(self, image:np.array)->np.ndarray:
        pass

    def preFFT(self, img):
        """预处理，将灰度图转为频率图"""
        # # 格式转换
        # if img.shape[2] == 3:
        #     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # if img.shape[2] == 4:
        #     img = cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY)
        # 数据类型转换
        img_float32 = np.float32(img)
        # 傅里叶变换
        dft_img = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
        # 将0频率位子移动到中心
        dft_shifted_img = np.fft.fftshift(dft_img)
        return dft_shifted_img

    def iFFT(self, dft_img):
        """后处理，将频率图转化为灰度图"""
        img_result = np.fft.ifftshift(dft_img)
        img_result = cv2.idft(img_result)
        img_result = cv2.magnitude(img_result[:, :, 0], img_result[:, :, 1])
        cv2.normalize(img_result, img_result, 0, 255, cv2.NORM_MINMAX)
        # img_result = cv2.cvtColor(img_result, cv2.COLOR_GRAY2BGRA)
        return img_result

    def setFilterType(self, filterType:bool):
        if filterType == True:
            self.filterType = 'High'
        else:
            self.filterType = 'Low'
        self.componentAttributeUpdate.emit()

    def setHighFilter(self):
        self.setFilterType(True)

    def setLowFilter(self):
        self.setFilterType(False)