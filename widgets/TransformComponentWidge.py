# Form implementation generated from reading ui file 'TransformComponentWidge.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TransformComponentWidget(object):
    def setupUi(self, TransformComponentWidget):
        TransformComponentWidget.setObjectName("TransformComponentWidget")
        TransformComponentWidget.resize(357, 528)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(TransformComponentWidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(parent=TransformComponentWidget)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.enable = QtWidgets.QRadioButton(parent=self.widget)
        self.enable.setChecked(True)
        self.enable.setObjectName("enable")
        self.verticalLayout.addWidget(self.enable)
        self.verticalLayout_5.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=TransformComponentWidget)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_8 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_8)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_7 = QtWidgets.QLabel(parent=self.widget_8)
        self.label_7.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_7.setObjectName("label_7")
        self.horizontalLayout.addWidget(self.label_7)
        self.tranX = NamedSilder(parent=self.widget_8)
        self.tranX.setObjectName("tranX")
        self.horizontalLayout.addWidget(self.tranX)
        self.verticalLayout_2.addWidget(self.widget_8)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.tranY = NamedSilder(parent=self.widget_5)
        self.tranY.setObjectName("tranY")
        self.horizontalLayout_2.addWidget(self.tranY)
        self.verticalLayout_2.addWidget(self.widget_5)
        self.verticalLayout_5.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(parent=TransformComponentWidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.rotate = NamedSilder(parent=self.widget_3)
        self.rotate.setObjectName("rotate")
        self.verticalLayout_3.addWidget(self.rotate)
        self.verticalLayout_5.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(parent=TransformComponentWidget)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_4)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.scaleX = NamedSilder(parent=self.widget_4)
        self.scaleX.setObjectName("scaleX")
        self.verticalLayout_4.addWidget(self.scaleX)
        self.scaleY = NamedSilder(parent=self.widget_4)
        self.scaleY.setObjectName("scaleY")
        self.verticalLayout_4.addWidget(self.scaleY)
        self.verticalLayout_5.addWidget(self.widget_4)

        self.retranslateUi(TransformComponentWidget)
        QtCore.QMetaObject.connectSlotsByName(TransformComponentWidget)

    def retranslateUi(self, TransformComponentWidget):
        _translate = QtCore.QCoreApplication.translate
        TransformComponentWidget.setWindowTitle(_translate("TransformComponentWidget", "Form"))
        self.label.setText(_translate("TransformComponentWidget", "是否启用"))
        self.enable.setText(_translate("TransformComponentWidget", "Enable"))
        self.label_2.setText(_translate("TransformComponentWidget", "平移"))
        self.label_7.setText(_translate("TransformComponentWidget", "X轴："))
        self.label_5.setText(_translate("TransformComponentWidget", "Y轴："))
        self.label_3.setText(_translate("TransformComponentWidget", "旋转"))
        self.label_4.setText(_translate("TransformComponentWidget", "缩放"))
from widgets.utils.NamedSilder import NamedSilder