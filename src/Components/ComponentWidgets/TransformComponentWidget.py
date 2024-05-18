# name:Gong Xiaoyv
# Time  2024-05-15   14:20

from PyQt6.QtWidgets import QWidget

from widgets.TransformComponentWidge import Ui_TransformComponentWidget


class TransformComponentWidget(QWidget):
    def __init__(self, parent=None):
        super(TransformComponentWidget, self).__init__(parent)
        self.ui = Ui_TransformComponentWidget()
        self.ui.setupUi(self)

        self.ui.tranX.setName("translate X: ")
        self.ui.tranY.setName("translate Y: ")
        self.ui.tranX.setRangeAndK(-100,100,1)
        self.ui.tranY.setRangeAndK(-100,100,1)
        self.ui.tranX.setValue(0)
        self.ui.tranY.setValue(0)

        self.ui.scaleX.setName("Scale X: ")
        self.ui.scaleY.setName("Scale Y: ")
        self.ui.scaleX.setRangeAndK(1,10,0.1)
        self.ui.scaleY.setRangeAndK(1,10,0.1)
        self.ui.scaleX.setValue(1)
        self.ui.scaleY.setValue(1)

        self.ui.rotate.setName("Rotate: ")
        self.ui.rotate.setRangeAndK(0,360,1)
        self.ui.rotate.setValue(0)
