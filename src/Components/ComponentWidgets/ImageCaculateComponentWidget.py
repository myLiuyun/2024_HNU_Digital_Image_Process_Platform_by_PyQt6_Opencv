# name:Gong Xiaoyv
# Time  2024-05-14   3:48
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal, QUrl
from widgets.ImageCaculateComponent import Ui_ImageCaculateComponent
from PyQt6.QtWidgets import QFileDialog
from src.Image import Image

class ImageCaculateComponentWidget(QtWidgets.QWidget):
    loadImage = pyqtSignal(object) # Image
    def __init__(self, parent=None):
        super(ImageCaculateComponentWidget, self).__init__(parent)
        self.ui = Ui_ImageCaculateComponent()
        self.ui.setupUi(self)
        self.ui.openfile.clicked.connect(self.readFileAndLoadImage)

    def readFileAndLoadImage(self):

        file_path,file_type = QFileDialog.getOpenFileUrl(self, "打开filter文件",
                                                         QUrl("jetbrains://pycharm/navigate/reference?project=Py_digital_img_process_platform&path=test_datas"))
        file_path = file_path.toLocalFile()
        self.ui.currentImg.setText(file_path)
        image = Image(file_path)
        self.loadImage.emit(image)