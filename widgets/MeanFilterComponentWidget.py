# Form implementation generated from reading ui file 'MeanFilterComponentWidget.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 395)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 60))
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
        self.verticalLayout_4.addWidget(self.widget)
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.arithmetic = QtWidgets.QRadioButton(parent=self.widget_3)
        self.arithmetic.setChecked(True)
        self.arithmetic.setObjectName("arithmetic")
        self.verticalLayout_3.addWidget(self.arithmetic)
        self.geometric = QtWidgets.QRadioButton(parent=self.widget_3)
        self.geometric.setObjectName("geometric")
        self.verticalLayout_3.addWidget(self.geometric)
        self.harmonic = QtWidgets.QRadioButton(parent=self.widget_3)
        self.harmonic.setObjectName("harmonic")
        self.verticalLayout_3.addWidget(self.harmonic)
        self.contra_harmonic = QtWidgets.QRadioButton(parent=self.widget_3)
        self.contra_harmonic.setObjectName("contra_harmonic")
        self.verticalLayout_3.addWidget(self.contra_harmonic)
        self.widget_5 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_5)
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.Q = QtWidgets.QSpinBox(parent=self.widget_5)
        self.Q.setMinimum(-5)
        self.Q.setMaximum(5)
        self.Q.setSingleStep(1)
        self.Q.setProperty("value", 1)
        self.Q.setObjectName("Q")
        self.horizontalLayout.addWidget(self.Q)
        self.verticalLayout_3.addWidget(self.widget_5)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_6)
        font = QtGui.QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.K = QtWidgets.QSpinBox(parent=self.widget_6)
        self.K.setMinimum(3)
        self.K.setMaximum(33)
        self.K.setSingleStep(2)
        self.K.setObjectName("K")
        self.horizontalLayout_2.addWidget(self.K)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_4.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "是否启用"))
        self.enable.setText(_translate("Form", "Enable"))
        self.label_2.setText(_translate("Form", "滤波器种类"))
        self.arithmetic.setText(_translate("Form", "算数均值滤波器"))
        self.geometric.setText(_translate("Form", "几何均值滤波器"))
        self.harmonic.setText(_translate("Form", "谐波滤波器"))
        self.contra_harmonic.setText(_translate("Form", "逆谐波滤波器"))
        self.label_4.setText(_translate("Form", "阶数："))
        self.label_3.setText(_translate("Form", "滤波器大小"))
