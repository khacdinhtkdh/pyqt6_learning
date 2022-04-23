import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        hbox = QHBoxLayout()

        btn1 = QPushButton('click one')
        btn2 = QPushButton('click two')
        btn3 = QPushButton('click three')
        btn4 = QPushButton('click four')
        self.setLayout(hbox)
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        # hbox.addSpacing(100)
        hbox.addStretch(5)


app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

