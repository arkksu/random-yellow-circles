from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint
from ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.createbutton.clicked.connect(self.createEvent)
        self.flag = False
        self.c = []

    def createEvent(self):
        d = randint(10, min(self.width(), self.height()) // 2)
        x = randint(0, self.width() - d)
        y = randint(0, self.height() - d)
        self.c.append((QColor(randint(0, 255), randint(0, 255), randint(0, 255)), [x, y, d, d]))
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            painter = QPainter(self)
            for circle in self.c:
                painter.setBrush(circle[0])
                painter.drawEllipse(*circle[1])


if __name__ == '__main__':
    app = QApplication(argv)
    window = MainWindow()
    window.show()
    exit(app.exec())
