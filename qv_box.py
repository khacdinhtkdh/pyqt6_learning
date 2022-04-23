import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        vbox = QVBoxLayout()

        btn1 = QPushButton('click one')
        btn2 = QPushButton('click two')
        btn3 = QPushButton('click three')
        btn4 = QPushButton('click four')
        self.setLayout(vbox)
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)
        vbox.addWidget(btn4)
        # hbox.addSpacing(100)
        vbox.addStretch(10)


app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

