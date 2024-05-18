# name:Gong Xiaoyv
# Time  2024-05-13   18:45
from PyQt6.QtWidgets import QWidget
from widgets.SortedFilterComponentWidget import Ui_SortedFilterWidget

class SortedFilterComponentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SortedFilterWidget()
        self.ui.setupUi(self)
