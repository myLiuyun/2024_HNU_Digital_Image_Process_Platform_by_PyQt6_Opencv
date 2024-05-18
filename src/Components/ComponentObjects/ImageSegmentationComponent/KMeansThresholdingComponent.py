# name:Gong Xiaoyv
# Time  2024-05-14   10:59

from src.Components.Component import Component
import cv2
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QWidget,QGridLayout,QPushButton,QGroupBox,QRadioButton
from src.Image import Image
from PyQt6.QtCore import pyqtSignal
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QPushButton,QGroupBox,QRadioButton
import numpy as np

from src.Components.ComponentWidgets.KmeansComponentWidget import KMeansThresholdingComponentWidget

class KMeansThresholdingComponent(Component):
    name = 'KMeansThresholdingComponent'
    detail = '使用3维RGB数据的Kmeans聚类方式，进行图像分割'
    def __init__(self, parent=None):
        super().__init__(parent)
        self.controlWidget = KMeansThresholdingComponentWidget()
        self.k = 2
        """信号和槽"""
        self.controlWidget.ui.enable.clicked.connect(self.setEnabel)
        self.controlWidget.ui.k.valueChanged.connect(self.setK)

    def processImage(self, image: np.array) -> np.ndarray:
        src = image
        if image.shape[2]==4:
            src = cv2.cvtColor(image, cv2.COLOR_BGRA2BGR)
        # 将图像转换为一维向量
        pixel_values = src.reshape(-1, 3).astype(np.float32)
        # 运行K-means算法
        """
        参数：
        data:  需要分类数据，最好是np.float32的数据，每个特征放一列。
        K:  聚类个数 
        criteria：迭代停止的模式选择，这是一个含有三个元素的元组型数。格式为（type, max_iter, epsilon） 其中，type有如下模式：
            cv2.TERM_CRITERIA_EPS ：精确度（误差）满足epsilon，则停止。
            cv2.TERM_CRITERIA_MAX_ITER：迭代次数超过max_iter，则停止。
            cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER：两者结合，满足任意一个结束。
        attempts：重复试验kmeans算法次数，将会返回最好的一次结果
        flags：初始中心选择，可选以下两种：
            v2.KMEANS_PP_CENTERS：使用kmeans++算法的中心初始化算法，即初始中心的选择使眼色相差最大.详细可查阅kmeans++算法。(Use kmeans++ center initialization by Arthur and Vassilvitskii)
            cv2.KMEANS_RANDOM_CENTERS：每次随机选择初始中心（Select random initial centers in each attempt.）
        
        返回值：
        compactness：紧密度，返回每个点到相应重心的距离的平方和
        labels：结果标记，每个成员被标记为分组的序号，如 0,1,2,3,4...等
        centers：由聚类的中心组成的数组
        """
        criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.1)
        _, labels, centers = cv2.kmeans(pixel_values, self.k, None, criteria, 10, cv2.KMEANS_PP_CENTERS)
        centers = np.uint8(centers)
        labels = labels.flatten()

        # 将每个像素分配到最近的聚类中心
        segmented_image = centers[labels.flatten()]
        segmented_image = segmented_image.reshape(src.shape)
        return segmented_image

    def setK(self,val):
        self.k = val
        self.componentAttributeUpdate.emit()


