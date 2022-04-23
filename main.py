import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        label = QLabel('Python Pyqt6', self)

        label.setFont(QFont('Sanserif', 14))
        label.setStyleSheet('color:red')
        label.setText("hello word")



app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

