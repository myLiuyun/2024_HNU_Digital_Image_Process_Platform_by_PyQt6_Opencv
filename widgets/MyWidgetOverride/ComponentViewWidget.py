# name:Gong Xiaoyv
# Time  2024-05-07   8:50
from PyQt6.QtCore import Qt,QMimeData
from PyQt6.QtGui import QDrag
from PyQt6.QtWidgets import QTreeWidget, QTreeWidgetItem, QAbstractItemView
from src.Components.ComponentFactory import ComponentFactory
from src.Components.Component import Component
# from PyQt6.QtCore import QDrog

class ComponentViewWidget(QTreeWidget):

    def __init__(self, parent=None):
        super(ComponentViewWidget, self).__init__(parent)
        self.setColumnCount(1)
        # 允许拖出
        self.setDragDropMode(QAbstractItemView.DragDropMode.DragOnly)
        self.setAcceptDrops(False)
        # 初始化Items
        for key in ComponentFactory.component_name_map.keys():
            top_item = QTreeWidgetItem(self)
            top_item.setText(0, key)
            for component_name in ComponentFactory.component_name_map[key]:
                node = QTreeWidgetItem(top_item)
                node.setText(0, component_name)
                if component_name in ComponentFactory.conponent_detail_key:
                    node.setToolTip(0,ComponentFactory.conponent_detail_key[component_name])
                top_item.addChild(node)
            self.addTopLevelItem(top_item)

    def mousePressEvent(self, event):
        """点击时处理拖拽事件，发送Item的text内容"""
        if event.button() == Qt.MouseButton.LeftButton:
            index = self.currentIndex()
            if index.isValid():
                item = self.itemFromIndex(index)
                if item.childCount() == 0:
                    # 获取content，传递出去
                    drag = QDrag(self)
                    mimedata = QMimeData()
                    mimedata.setText(item.text(0))  # 放入数据
                    drag.setMimeData(mimedata)
                    dropAction = drag.exec(Qt.DropAction.MoveAction) # 异步执行拖拽事件
        super(ComponentViewWidget, self).mousePressEvent(event)