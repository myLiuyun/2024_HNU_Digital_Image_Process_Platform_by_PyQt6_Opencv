# Form implementation generated from reading ui file 'SaveImageWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SaveImageWidget(object):
    def setupUi(self, SaveImageWidget):
        SaveImageWidget.setObjectName("SaveImageWidget")
        SaveImageWidget.resize(320, 240)
        self.verticalLayout = QtWidgets.QVBoxLayout(SaveImageWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(parent=SaveImageWidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.shape = QtWidgets.QLabel(parent=self.widget)
        self.shape.setObjectName("shape")
        self.horizontalLayout.addWidget(self.shape)
        self.verticalLayout.addWidget(self.widget)
        self.widget_3 = QtWidgets.QWidget(parent=SaveImageWidget)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.format = QtWidgets.QComboBox(parent=self.widget_3)
        self.format.setObjectName("format")
        self.format.addItem("")
        self.format.addItem("")
        self.format.addItem("")
        self.horizontalLayout_3.addWidget(self.format)
        self.verticalLayout.addWidget(self.widget_3)
        self.save = QtWidgets.QPushButton(parent=SaveImageWidget)
        self.save.setObjectName("save")
        self.verticalLayout.addWidget(self.save)

        self.retranslateUi(SaveImageWidget)
        QtCore.QMetaObject.connectSlotsByName(SaveImageWidget)

    def retranslateUi(self, SaveImageWidget):
        _translate = QtCore.QCoreApplication.translate
        SaveImageWidget.setWindowTitle(_translate("SaveImageWidget", "Form"))
        self.label.setText(_translate("SaveImageWidget", "分辨率："))
        self.shape.setText(_translate("SaveImageWidget", "None"))
        self.label_2.setText(_translate("SaveImageWidget", "文件格式："))
        self.format.setItemText(0, _translate("SaveImageWidget", ".png"))
        self.format.setItemText(1, _translate("SaveImageWidget", ".jpg"))
        self.format.setItemText(2, _translate("SaveImageWidget", ".webp"))
        self.save.setText(_translate("SaveImageWidget", "保存"))
