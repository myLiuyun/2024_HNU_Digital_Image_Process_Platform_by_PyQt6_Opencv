# name:Gong Xiaoyv
# Time  2024-05-14   0:11

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import Qt, pyqtSignal
from widgets.GradientFilterComponentWidget import Ui_GradientFiterComponentWidget


class GradientFilterComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(GradientFilterComponentWidget, self).__init__(parent)
        self.ui = Ui_GradientFiterComponentWidget()
        self.ui.setupUi(self)
        """设置互斥"""
        radioBox = QtWidgets.QButtonGroup(self)
        radioBox.setExclusive(True)
        radioBox.addButton(self.ui.Laplacian)
        radioBox.addButton(self.ui.Sobel)
        radioBox.addButton(self.ui.Robert)
        radioBox.addButton(self.ui.Prewitt)
        self.ui.Laplacian.toggled.connect(self.initTwoRadioButtons)


    def initTwoRadioButtons(self, flag: bool):
        if flag:
            self.ui.Fore.setEnabled(True)
            self.ui.Eight.setEnabled(True)
        else:
            self.ui.Fore.setEnabled(False)
            self.ui.Eight.setEnabled(False)
            # self.ui.Fore.setChecked(False)
            # self.ui.Eight.setChecked(False)