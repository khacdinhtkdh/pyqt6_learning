import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.lb = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()
        btn1 = QPushButton('change text')
        btn1.clicked.connect(self.click_btn)
        self.lb = QLabel('Default text')

        hbox.addWidget(btn1)
        hbox.addWidget(self.lb)
        self.setLayout(hbox)

    def click_btn(self):
        self.lb.setText('KD SHIN')
        self.lb.setFont(QFont('Times', 12))






app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

