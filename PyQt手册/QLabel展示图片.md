

```python
class TestWin(QMainWindow):
    def __init__(self, parent=None):
        super(TestWin, self).__init__(parent)
        self.resize(1000,400)
        label = QLabel()
        label.setFixedSize(1000, 400)
        pixmap = QPixmap("E:\我的坚果云\Mapixel\lyric_background.jpg")
        label.setPixmap(pixmap)
        self.setCentralWidget(label)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TestWin()
    main.show()
    sys.exit(app.exec_())
```

