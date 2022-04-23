import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")
        self.create_button()

    def create_button(self):
        btn = QPushButton('click', self)
        btn.setGeometry(50, 40, 100, 50)
        btn.setFont(QFont('Times', 15, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon('image/icon.png'))
        btn.setIconSize(QSize(36, 36))

        menu = QMenu()
        menu.addAction('copy')
        menu.addAction('cut')
        menu.addAction('paste')
        btn.setMenu(menu)


app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

