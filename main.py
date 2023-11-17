from sys import argv, exit
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.createbutton.clicked.connect(self.createEvent)
        self.flag = False
        self.c = []

    def createEvent(self):
        d = random.randint(10, min(self.width(), self.height()) // 2)
        x = random.randint(0, self.width() - d)
        y = random.randint(0, self.height() - d)
        self.c.append([x, y, d, d])
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            painter.setBrush(QColor(255, 255, 0))
            for circle in self.c:
                painter.drawEllipse(*circle)


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
