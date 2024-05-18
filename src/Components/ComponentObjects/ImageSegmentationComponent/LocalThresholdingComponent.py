# name:Gong Xiaoyv
# Time  2024-05-14   9:33

from src.Components.Component import Component
import cv2
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
from src.Image import Image
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton,QGroupBox,QRadioButton
import numpy as np
from src.Components.ComponentWidgets.LocalThresholdingComponentWidget import LocalThresholdingComponentWidget

class LocalThresholdingComponent(Component):
    name = 'LocalThresholdingComponent'
    detail = '局部阈值分割，分割为前景和背景，前景为黑，背景为白'
    def __init__(self, parent=None):
        super(LocalThresholdingComponent, self).__init__(parent)
        self.controlWidget = LocalThresholdingComponentWidget()
        self.blockNum = [1,1] # 当设置为1,1,等于效果等于全局阈值分割

        """信号和槽"""
        self.controlWidget.ui.enable.clicked.connect(self.setEnabel)
        self.controlWidget.ui.x.valueChanged.connect(self.setBlockNumX)
        self.controlWidget.ui.y.valueChanged.connect(self.setBlockNumY)

    def processImage(self, image: np.array) -> np.ndarray:
        h,w = image.shape[:2]
        if image.shape[2]==4:
            grey = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
        elif image.shape[2]==3:
            grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            raise Exception("nLocalThresholdingComponent: ot valid image shape")
        procesed_grey = grey.copy()
        """进行图像切分"""
        step_width = int( w / self.blockNum[0] )
        step_height = int( h / self.blockNum[1] )
        for i in range(0,self.blockNum[0]):
            for j in range(0,self.blockNum[1]):
                img_block = grey[j*step_height: (j+1)*step_height, i*step_width: (i+1)*step_width]
                procesed_grey[j*step_height: (j+1)*step_height,i*step_width: (i+1)*step_width] = self.ThresholdWholeImage(img_block)
        procesed_grey = cv2.cvtColor(procesed_grey, cv2.COLOR_GRAY2BGRA)
        return procesed_grey


    def ThresholdWholeImage(self, image: np.array) -> np.array:
        thresh = self.threshold_two_peak(image)
        threshImage = image.copy()
        threshImage[threshImage > thresh] = 255
        threshImage[threshImage <= thresh] = 0
        print(f"阈值为{thresh}")
        # self.showImageOpenCv(threshImage)
        # 灰度图转BGAR

        return threshImage

    def threshold_two_peak(self, image: np.ndarray):
        """
        寻找两个峰值之间的最低点，作为分隔阈值
        :image 灰度图
        :return
        """
        # 计算灰度直方图
        histogram = self.calcGrayHist(image)
        # 找到灰度直方图的最大峰值对应的灰度值
        maxLoc = np.where(histogram == np.max(histogram[:255]))
        firstPeak = maxLoc[0][0]
        # 寻找灰度直方图的第二个峰值对应的灰度值,计算度量量：与第一个峰值最远且出现频率较高的灰度值,
        measureDists = np.zeros([256], np.float32)
        for k in range(250):
            measureDists[k] = pow(k - firstPeak, 2) * histogram[k]
        maxLoc2 = np.where(measureDists == np.max(measureDists))
        secondPeak = maxLoc2[0][0]
        print(f"firstPeak: {firstPeak}, secondPeak: {secondPeak}")
        # 找到两个峰值之间的最小值对应的灰度值，作为阈值
        thresh = 0
        if firstPeak > secondPeak:  # 第一个峰值在第二个峰值的右侧
            temp = histogram[int(secondPeak):int(firstPeak)]
            minLoc = np.where(temp == np.min(temp))
            thresh = secondPeak + minLoc[0][0] + 1
        else:  # 第一个峰值在第二个峰值的右侧
            temp = histogram[int(firstPeak):int(secondPeak)]
            minLoc = np.where(temp == np.min(temp))
            thresh = firstPeak + minLoc[0][0] + 1
        return thresh

    def calcGrayHist(self,I):
        # 计算灰度直方图
        h, w = I.shape[:2]
        grayHist = np.zeros([256], np.uint64)
        for i in range(h):
            for j in range(w):
                grayHist[I[i][j]] += 1
        return grayHist

    def setBlockNumX(self, val):
        self.blockNum[0] = val
        self.componentAttributeUpdate.emit()

    def setBlockNumY(self, val):
        self.blockNum[1] = val
        self.componentAttributeUpdate.emit()