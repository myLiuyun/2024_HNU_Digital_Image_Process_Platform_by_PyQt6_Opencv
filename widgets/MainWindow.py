# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 575)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(400, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.groupBox)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 398, 498))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")
        self.componentWidget = AttributeWidget(parent=self.scrollAreaWidgetContents)
        self.componentWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.componentWidget.setObjectName("componentWidget")
        self.basic_page = QtWidgets.QWidget()
        self.basic_page.setGeometry(QtCore.QRect(0, 0, 380, 450))
        self.basic_page.setObjectName("basic_page")
        self.componentWidget.addItem(self.basic_page, "")
        self.verticalLayout.addWidget(self.componentWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(400, 0))
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 2, 0, 1, 1)
        self.processedImageArea = ImageShowArea(parent=self.groupBox_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.processedImageArea.setPalette(palette)
        self.processedImageArea.setAutoFillBackground(True)
        self.processedImageArea.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.processedImageArea.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.processedImageArea.setText("")
        self.processedImageArea.setObjectName("processedImageArea")
        self.gridLayout_2.addWidget(self.processedImageArea, 1, 0, 1, 1)
        self.sourceImageArea = ImageShowArea(parent=self.groupBox_2)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        self.sourceImageArea.setPalette(palette)
        self.sourceImageArea.setAutoFillBackground(True)
        self.sourceImageArea.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.sourceImageArea.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.sourceImageArea.setText("")
        self.sourceImageArea.setObjectName("sourceImageArea")
        self.gridLayout_2.addWidget(self.sourceImageArea, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setMinimumSize(QtCore.QSize(200, 0))
        self.groupBox_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.componentTreeView = ComponentViewWidget(parent=self.groupBox_3)
        self.componentTreeView.setMaximumSize(QtCore.QSize(500, 16777215))
        self.componentTreeView.setObjectName("componentTreeView")
        self.componentTreeView.headerItem().setText(0, "All Comonent")
        self.gridLayout_3.addWidget(self.componentTreeView, 0, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1030, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(parent=self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen = QtGui.QAction(parent=MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionsave = QtGui.QAction(parent=MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionexit = QtGui.QAction(parent=MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.menu.addAction(self.actionopen)
        self.menu.addAction(self.actionsave)
        self.menu.addSeparator()
        self.menu.addAction(self.actionexit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.componentWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Components"))
        self.groupBox_2.setTitle(_translate("MainWindow", "View"))
        self.label_2.setText(_translate("MainWindow", "Source Image"))
        self.label.setText(_translate("MainWindow", "Processed Image"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Components"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
from widgets.MyWidgetOverride.AttributeWidget import AttributeWidget
from widgets.MyWidgetOverride.ComponentViewWidget import ComponentViewWidget
from widgets.MyWidgetOverride.ImageShowArea import ImageShowArea