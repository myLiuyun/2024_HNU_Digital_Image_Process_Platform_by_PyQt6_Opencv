# name:Gong Xiaoyv
# Time  2024-05-13   19:58
import cv2
import numpy as np

from src.Components.Component import Component

from src.Components.ComponentWidgets import GradientFilterComponentWidget


class GradientFilterComponent(Component):
    name = 'Gradient Filter Component'
    detail = "微分滤波器，实现锐化，可选拉 Robert/Laplacian/Prewitt/Sobel 滤波、"
    def __init__(self,parent=None):
        super().__init__(parent)
        self.controlWidget = GradientFilterComponentWidget.GradientFilterComponentWidget()

        # Robert / Laplacian
        self.FliterType = 'Laplacian'
        self.FliterIdx = 0 # 两个滤波器，对拉普普拉斯，代表4/8连通
        """信号和槽"""
        self.controlWidget.ui.enableButton.toggled.connect(self.setEnabel)
        self.controlWidget.ui.Laplacian.toggled.connect(self.setLaplacianFilterType)
        self.controlWidget.ui.Sobel.toggled.connect(self.setSobelFilterType)
        self.controlWidget.ui.Prewitt.toggled.connect(self.setPrewittFilterType)
        self.controlWidget.ui.Robert.toggled.connect(self.setRobertFilterType)
        self.controlWidget.ui.Fore.toggled.connect(self.setLaplacianFilterIdx0)
        self.controlWidget.ui.Eight.toggled.connect(self.setLaplacianFilterIdx1)

    def processImage(self, image:np.array)->np.ndarray:
        src = image
        if image.shape[2] == 4:
            src = cv2.cvtColor(image, cv2.COLOR_BGRA2RGB)
        processed = np.zeros_like(src)
        # 四种滤波器，拉普拉斯直接返回，其余的需要在两个方向分别滤波，再叠加
        if self.FliterType == 'Laplacian':
            fliter1 = self.getFilter()
            fliter2 = self.getFilter()
        else:
            self.FliterIdx = 0
            fliter1 = self.getFilter()
            self.FliterIdx = 1
            fliter2 = self.getFilter()
        # 两个滤波器分别滤波，再叠加
        processed1 = cv2.filter2D(src, -1, fliter1)
        processed2 = cv2.filter2D(src, -1, fliter2)
        processed = cv2.addWeighted(processed1, 0.5, processed2, 0.5, 0)
        if processed.shape[2]==3:
            processed = cv2.cvtColor(processed, cv2.COLOR_RGB2BGRA)
        return processed

    def getFilter(self)->np.ndarray:
        if self.FliterType == 'Robert':
            if self.FliterIdx == 0:
                return np.array([[-1,0],
                                 [0,1]])
            if self.FliterIdx == 1:
                return np.array([[0,-1],
                                   [1,0]])
        elif self.FliterType == 'Laplacian':
            if self.FliterIdx == 0:
                return np.array([[0,-1,0],
                                   [-1,4,-1],
                                   [0,-1,0]])
            elif self.FliterIdx == 1:
                return np.array([[-1,-1,-1],
                                   [-1,8,-1],
                                   [-1,-1,-1]])
        elif self.FliterType == 'Sobel':
            if self.FliterIdx == 0:
                return np.array([[1,0,-1],
                                   [2,0,-2],
                                   [1,0,-1]])
            elif self.FliterIdx == 1:
                return np.array([[-1,-2,-1],
                                   [0,0,0],
                                   [1,2,1]])
        elif self.FliterType == "Prewitt":
            if self.FliterIdx == 0:
                return np.array([[1,0, -1],
                                   [1,0,-1],
                                   [1,0,-1]])
            elif self.FliterIdx == 1:
                return np.array([[-1,-1,-1],
                                   [0,0,0],
                                   [1,1,1]])
        else:
            raise Exception("no such Gradient filter")


    def setFilterType(self,filterType: str)->None:
        self.FliterType = filterType
        self.componentAttributeUpdate.emit()

    def setFilterIdx(self,filterIdx: int)->None:
        self.FliterIdx = filterIdx
        self.componentAttributeUpdate.emit()

    def setRobertFilterType(self)->None:
        self.setFilterType('Robert')

    def setLaplacianFilterType(self)->None:
        self.setFilterType('Laplacian')

    def setSobelFilterType(self)->None:
        self.setFilterType('Sobel')

    def setPrewittFilterType(self)->None:
        self.setFilterType('Prewitt')

    def setLaplacianFilterIdx0(self)->None:
        self.setFilterIdx(0)

    def setLaplacianFilterIdx1(self)->None:
        self.setFilterIdx(1)