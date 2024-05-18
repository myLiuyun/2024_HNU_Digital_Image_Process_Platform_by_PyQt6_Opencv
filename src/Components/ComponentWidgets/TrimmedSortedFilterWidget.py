# name:Gong Xiaoyv
# Time  2024-05-15   20:55

from PyQt6.QtWidgets import QWidget
from widgets.TrimmedSortedFilterWidget import Ui_TrimmedSortedFilterWidget

class TrimmedSortedFilterWidget(QWidget):
    def __init__(self, parent=None):
        super(TrimmedSortedFilterWidget, self).__init__(parent)
        self.ui = Ui_TrimmedSortedFilterWidget()
        self.ui.setupUi(self)