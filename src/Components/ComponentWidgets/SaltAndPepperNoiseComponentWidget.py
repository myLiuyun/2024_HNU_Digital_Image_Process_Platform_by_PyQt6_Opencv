# name:Gong Xiaoyv
# Time  2024-05-15   20:19
from PyQt6 import QtCore, QtGui, QtWidgets
from widgets.SaltAndPepperNoiseComponentWidget import Ui_SaltAndPepperNoiseComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal

class SaltAndPepperNoiseComponentWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SaltAndPepperNoiseComponentWidget, self).__init__(parent)
        self.ui = Ui_SaltAndPepperNoiseComponentWidget()
        self.ui.setupUi(self)