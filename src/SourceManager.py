# name:Gong Xiaoyv
# Time  2024-05-06   17:48
from PyQt6.QtCore import QObject

from src.Image import Image

class SourceManager(QObject):
    def __init__(self,parent=None):
        super(SourceManager, self).__init__(parent)
        self.sourceImage = list()

    def addImage(self, image:Image) -> None:
        self.sourceImage.append(image)

