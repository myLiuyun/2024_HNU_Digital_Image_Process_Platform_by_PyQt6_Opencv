# name:Gong Xiaoyv
# Time  2024-05-06   17:02
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtGui import QImage,QPixmap
from PyQt6.QtWidgets import QWidget,QLabel
from src.Components.ComponentFactory import ComponentFactory
from src.Components.Component import Component
from src.Image import Image

class ImageShowArea(QLabel):
    """Signals"""
    addComponentSignal = pyqtSignal(Component) # 向图片添加了一个Component

    def __init__(self,parent=None):
        super(ImageShowArea,self).__init__(parent)
        # 允许拖拽
        self.setAcceptDrops(True)
        # 属性
        self.currentImage : Image = None
        self.currentPixmap : QPixmap = None
        self.sourceImageShowWidget : bool = True
        """初始化信号和槽"""
        self.initSignalsAndSlots()

    def updateCurrentImage(self, image:Image):
        if image != None:
            imagePixmap = QPixmap()
            if self.sourceImageShowWidget == True:
                imagePixmap = image.getSourceImagePixmap()
            else:
                iamgePixmap = image.getProcesedImagePixmap()
            self.currentImage = image
            self.currentPixmap = imagePixmap
            """连接Signal，监听Image的信号改变"""
            self.currentImage.imageComponentUpdadte.connect(self.updateShowImage)

            self.updateShowImage()
        else:
            print("none imgPixmap or image to pain")

    def dragEnterEvent(self, event):
        """
        判断是否接受事件，如果含有Text内容，则接受，否则不接受
        """
        if event.mimeData().hasText() and self.currentImage != None and self.sourceImageShowWidget==True:
            event.acceptProposedAction()
        else:
            event.ignore()

    def dropEvent(self, event):
        """
        松开拖拽事件时触发，用于添加控件
        """
        print(f"end drop, receive {event.mimeData().text()}")
        text = event.mimeData().text()
        componentFactory = ComponentFactory()
        component = componentFactory.createComponent(text)
        if component != None:
            self.currentImage.addComponent(component)
            # print(f"add compoent : {component.name}")
            self.addComponentSignal.emit(component)
            print(f"emit signal addComponentSignal")
        event.accept()

    def initSignalsAndSlots(self):
        pass
        # self.addComponentSignal.connect(self.updateShowImage)

    def updateShowImage(self):
        """重绘图片"""
        # print("Image show Area Update")
        width = self.size().width()
        height = self.size().height()
        if self.sourceImageShowWidget == True:
            self.setPixmap(self.currentImage.getSourceImagePixmap().scaled(width*0.95,height*0.95,
                                                                           aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))
        else:
            self.setPixmap(self.currentImage.getProcesedImagePixmap().scaled(width*0.95,height*0.95,
                                                                           aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))

    def resizeEvent(self, a0):
        if self.currentImage != None:
            self.updateShowImage()
