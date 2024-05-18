# name:Gong Xiaoyv
# Time  2024-04-28   10:10

import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from PyQt6.QtCore import pyqtSignal,QUrl

from widgets.MainWindow import Ui_MainWindow

from src.SourceManager import SourceManager
from src.Image import Image
from src.SaveImageWidget import SaveImageWidget


class MyApp(QMainWindow):
    """定义signals"""
    afterLoadImage = pyqtSignal(object)  # 参数为Image

    def __init__(self,parent=None, ui=None):
        super().__init__(parent=parent)
        self.setupUi(ui)
        """设置标题"""
        self.setWindowTitle('Opencv图像处理')
        self.setWindowIcon(QIcon('icons/main.png'))
        self.ui = ui
        """初始化信号和槽函数"""
        self.initSignals()
        """初始化属性"""
        self.sourceManager = SourceManager()

    def setupUi(self, ui):
        """
        初始化Ui
        :param ui: 一个Ui_Widget对象，调用其setupUi()，初始化该Widget的Ui
        :return: None
        """
        if ui!=None:
            ui.setupUi(self)
            ui.processedImageArea.sourceImageShowWidget = False
        else:
            print("Main Window ui=none")

    def initSignals(self):
        """
        初始化所有信号和槽的连接
        """
        """ 打开图片Action """
        self.ui.actionopen.triggered.connect(self.openImageDialog)
        """ 拖拽控件后，将对应控件和Widget加入到左侧Attribute栏 """
        self.ui.sourceImageArea.addComponentSignal.connect(self.ui.componentWidget.addComponent)
        """ 加载图片后，更新显示区域引用的Image对象 """
        self.afterLoadImage.connect(self.ui.sourceImageArea.updateCurrentImage)
        self.afterLoadImage.connect(self.ui.processedImageArea.updateCurrentImage)
        """ 添加控件后，重绘图片 """
        self.ui.sourceImageArea.addComponentSignal.connect(self.ui.sourceImageArea.updateShowImage)
        self.ui.sourceImageArea.addComponentSignal.connect(self.ui.processedImageArea.updateShowImage)
        """ 由于Component数量不一定，更改控件属性后重绘图片的逻辑，在Image::addComponent中实现"""
        """ 保存图像 """
        self.ui.actionsave.triggered.connect(self.saveImage)

    def openImageDialog(self):
        file_path,file_type = QFileDialog.getOpenFileUrl(self, "打开图片", QUrl("jetbrains://pycharm/navigate/reference?project=Py_digital_img_process_platform&path=test_datas"))
        print(file_path.path()[1::])
        file_path = file_path.path()[1::]
        image = Image(img_path = file_path)

        # image:QImage = QImage(file_path.path()[1::])
        if not image.isNull():
            # 加载图片成功，资源添加到sourceManager，并展示加载的图片
            print("set image")
            # self.ui.sourceImageArea.updateCurrentImage(imgPixmap=image.getSourceImagePixmap(),image=image)
            self.afterLoadImage.emit(image)
            # # 添加一个GuassianBlur
            # gaussianBlur = GaussianBlurComponent.GaussianBlurComponent()
            # image.addComponent(gaussianBlur)
            # self.afterAddComponent.emit(gaussianBlur)
            # self.ui.processedImageArea.updateCurrentImage(imgPixmap=image.getProcesedImagePixmap(),image=image)

    def saveImage(self):
        widget = SaveImageWidget(self)
        widget.setImage(self.ui.processedImageArea.currentImage)
        widget.show()

if __name__ == '__main__':
    # 生成一个Application对象
    app = QtWidgets.QApplication(sys.argv)
    # 生成MainWindow
    #main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    main_window = MyApp(ui=ui)

    # 利用MainWindow.py的ui，初始化MainWindow的ui
    #ui = Ui_MainWindow()
    #ui.setupUi(main_window)
    # 展示main_window
    main_window.show()
    # 进入程序的主循环，并通过exit函数确保主循环安全结束(该释放资源的一定要释放)
    sys.exit(app.exec())

