# name:Gong Xiaoyv
# Time  2024-05-14   8:11
import cv2
from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.SaveImageWidget import Ui_SaveImageWidget
from src.Image import Image
from PyQt6.QtCore import Qt

class SaveImageWidget(QtWidgets.QWidget):
    formatList = ['.png','.jpg','.webp']
    def __init__(self, parent=None):
        super(SaveImageWidget, self).__init__(parent)
        self.ui = Ui_SaveImageWidget()
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.Window, True)
        self.shape = [0,0]
        self.img = None
        self.format = '.png'
        """信号和槽"""
        self.ui.save.clicked.connect(self.save)
        self.ui.format.currentIndexChanged.connect(self.currentIdxChange)

    def setImage(self, image:Image):
        if image is None:
            return
        self.img = image
        self.ui.shape.setText(str(self.img.sourceImage.shape[:2]))
    def save(self):
        if self.img is None:
            raise Exception(" no image to save")

        processedImage = self.img.getProcessedImage()

        if self.format == '.png':
            cv2.imwrite("result/result.png",processedImage)
        if self.format == '.jpg':
            cv2.imwrite("result/result.jpg",processedImage)
        if self.format == '.webp':
            cv2.imwrite("result/result.webp", processedImage)

    def currentIdxChange(self, idx):
        print("save format changed: "+self.formatList[idx])
        self.format = self.formatList[idx]

