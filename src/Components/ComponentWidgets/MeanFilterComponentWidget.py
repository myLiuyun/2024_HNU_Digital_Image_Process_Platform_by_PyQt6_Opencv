# name:Gong Xiaoyv
# Time  2024-05-15   19:53
from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.MeanFilterComponentWidget import Ui_Form
from PyQt6.QtCore import Qt, pyqtSignal

class MeanFilterComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MeanFilterComponentWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

