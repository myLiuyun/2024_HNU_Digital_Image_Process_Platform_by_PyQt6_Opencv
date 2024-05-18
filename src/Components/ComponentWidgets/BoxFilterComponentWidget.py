# name:Gong Xiaoyv
# Time  2024-05-14   0:45
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QFileDialog

from widgets.BoxFilterComponentWidget import Ui_BoxFilterComponentWidget
from PyQt6.QtCore import Qt, pyqtSignal, QUrl

import numpy as np

class BoxFilterComponentWidget(QtWidgets.QWidget):
    filterUpdateSignal = pyqtSignal()
    def __init__(self, parent=None):
        super(BoxFilterComponentWidget, self).__init__(parent)
        self.ui = Ui_BoxFilterComponentWidget()
        self.ui.setupUi(self)
        self.filter = np.array([1])
        """连接信号和槽"""
        self.ui.openfile.clicked.connect(self.readFileAndUpdateFilter)

    def readFileAndUpdateFilter(self):

        file_path,file_type = QFileDialog.getOpenFileUrl(self, "打开filter文件",
                                                         QUrl("jetbrains://pycharm/navigate/reference?project=Py_digital_img_process_platform&path=test_datas"))
        file_path = file_path.toLocalFile()
        numbers = []
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for line in lines:
                nums = [float(num) for num in line.strip().split()]
                numbers.append(nums)
        self.filter = np.array(numbers,dtype=np.float32)
        self.ui.filter.setText(self.getFilterText(numbers))
        self.filterUpdateSignal.emit()

    def getFilterText(self, numbers):
        filterText = ""
        for num in numbers:
            filterText += str(num) + " \n"
        return filterText

    def getFilterSumOne(self):
        """
        :return: 归一化的filter
        """
        sum = np.sum(self.filter)
        return np.divide(self.filter, sum)