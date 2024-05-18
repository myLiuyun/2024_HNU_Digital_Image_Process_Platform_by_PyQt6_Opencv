# name:Gong Xiaoyv
# Time  2024-05-14   2:04

from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog, QWidget

from widgets.FrequencyDomainComponentWidget import Ui_FrequencyDomainComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal

class FrequencyDomainFilterComponentWidget(QWidget):
    setHighSlided = pyqtSignal()
    setLowSlided = pyqtSignal()
    setParameter1 = pyqtSignal(int)
    setParameter2 = pyqtSignal(int)

    def __init__(self, parent=None):
        super(FrequencyDomainFilterComponentWidget, self).__init__(parent)
        self.ui = Ui_FrequencyDomainComponentWidget()
        self.ui.setupUi(self)
