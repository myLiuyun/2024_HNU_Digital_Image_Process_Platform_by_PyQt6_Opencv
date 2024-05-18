# name:Gong Xiaoyv
# Time  2024-05-14   9:17
from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.MirrorComponentWidget import Ui_MirrorComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal

class MirrorComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MirrorComponentWidget, self).__init__(parent)
        self.ui = Ui_MirrorComponentWidget()
        self.ui.setupUi(self)

