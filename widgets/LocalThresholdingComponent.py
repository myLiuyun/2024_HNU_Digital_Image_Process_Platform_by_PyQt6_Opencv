# Form implementation generated from reading ui file 'LocalThresholdingComponent.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(parent=Form)
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
        self.verticalLayout_3.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(parent=Form)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.widget_3 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.x = QtWidgets.QSpinBox(parent=self.widget_3)
        self.x.setMinimum(1)
        self.x.setMaximum(10)
        self.x.setObjectName("x")
        self.horizontalLayout.addWidget(self.x)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_4 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.y = QtWidgets.QSpinBox(parent=self.widget_4)
        self.y.setMinimum(1)
        self.y.setMaximum(10)
        self.y.setObjectName("y")
        self.horizontalLayout_2.addWidget(self.y)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.verticalLayout_3.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "是否启用"))
        self.enable.setText(_translate("Form", "Enable"))
        self.label_2.setText(_translate("Form", "分块大小"))
        self.label_3.setText(_translate("Form", "X方向："))
        self.label_4.setText(_translate("Form", "Y方向："))