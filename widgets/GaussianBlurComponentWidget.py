# Form implementation generated from reading ui file 'GaussianBlurComponentWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_GaussianBlurComponentWidget(object):
    def setupUi(self, GaussianBlurComponentWidget):
        GaussianBlurComponentWidget.setObjectName("GaussianBlurComponentWidget")
        GaussianBlurComponentWidget.resize(250, 130)
        GaussianBlurComponentWidget.setMinimumSize(QtCore.QSize(250, 130))
        GaussianBlurComponentWidget.setMaximumSize(QtCore.QSize(250, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(GaussianBlurComponentWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(parent=GaussianBlurComponentWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.enableButton = QtWidgets.QRadioButton(parent=self.groupBox)
        self.enableButton.setChecked(True)
        self.enableButton.setObjectName("enableButton")
        self.gridLayout.addWidget(self.enableButton, 0, 1, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.groupBox)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.kernal_x = QtWidgets.QSpinBox(parent=self.widget)
        self.kernal_x.setSingleStep(2)
        self.kernal_x.setProperty("value", 5)
        self.kernal_x.setObjectName("kernal_x")
        self.horizontalLayout.addWidget(self.kernal_x)
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.kernal_y = QtWidgets.QSpinBox(parent=self.widget)
        self.kernal_y.setSingleStep(2)
        self.kernal_y.setProperty("value", 5)
        self.kernal_y.setObjectName("kernal_y")
        self.horizontalLayout.addWidget(self.kernal_y)
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout.addWidget(self.widget, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(GaussianBlurComponentWidget)
        QtCore.QMetaObject.connectSlotsByName(GaussianBlurComponentWidget)

    def retranslateUi(self, GaussianBlurComponentWidget):
        _translate = QtCore.QCoreApplication.translate
        GaussianBlurComponentWidget.setWindowTitle(_translate("GaussianBlurComponentWidget", "Form"))
        self.groupBox.setTitle(_translate("GaussianBlurComponentWidget", "Gaussian Blur Component"))
        self.label.setText(_translate("GaussianBlurComponentWidget", "Kerbal size :"))
        self.enableButton.setText(_translate("GaussianBlurComponentWidget", "是否启用"))
        self.label_2.setText(_translate("GaussianBlurComponentWidget", "("))
        self.label_4.setText(_translate("GaussianBlurComponentWidget", ","))
        self.label_3.setText(_translate("GaussianBlurComponentWidget", ")"))
        self.label_5.setText(_translate("GaussianBlurComponentWidget", "Enable："))
