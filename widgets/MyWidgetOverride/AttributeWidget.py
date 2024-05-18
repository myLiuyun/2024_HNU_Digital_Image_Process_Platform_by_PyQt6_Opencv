# name:Gong Xiaoyv
# Time  2024-05-07   8:17

from PyQt6.QtWidgets import QToolBox, QWidget
from PyQt6.QtCore import pyqtSignal
from src import Components

class AttributeWidget(QToolBox):
    def __init__(self, parent=None):
        super(AttributeWidget, self).__init__(parent)
        self.setItemText(0,"")
        self.setCurrentIndex(-1)
        self.none = True

    def addComponent(self, component):
        # print(f'addComponent item :{component.getName()}')
        self.addItem(component.controlWidget, component.getName())
        if self.none:
            self.none = False
            self.removeItem(0)

