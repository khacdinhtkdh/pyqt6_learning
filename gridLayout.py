import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        grid = QGridLayout()
        btn1 = QPushButton('click one')
        btn2 = QPushButton('click two')
        btn3 = QPushButton('click three')
        btn4 = QPushButton('click four')
        btn5 = QPushButton('click five')
        btn6 = QPushButton('click six')
        btn7 = QPushButton('click seven')
        btn8 = QPushButton('click eight')

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 1, 0)
        grid.addWidget(btn5, 1, 1)
        grid.addWidget(btn6, 1, 2)
        grid.addWidget(btn7, 2, 0)
        grid.addWidget(btn8, 2, 1)

        self.setLayout(grid)

app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

