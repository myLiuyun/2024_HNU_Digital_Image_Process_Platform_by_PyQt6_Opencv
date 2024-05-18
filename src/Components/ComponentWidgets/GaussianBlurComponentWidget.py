# name:Gong Xiaoyv
# Time  2024-05-07   11:36

from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.GaussianBlurComponentWidget import Ui_GaussianBlurComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal

class GaussianBlurComponentWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GaussianBlurComponentWidget()
        self.ui.setupUi(self)

