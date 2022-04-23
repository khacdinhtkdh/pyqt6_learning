import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        line_edit = QLineEdit(self)
        line_edit.setFont(QFont('Times', 14))
        # line_edit.setText("default text")
        line_edit.setPlaceholderText('enter user name')
        #line_edit.setEnabled(False)
        line_edit.setEchoMode(QLineEdit.EchoMode.Password)


app = QApplication(sys.argv)
windown = Main()
windown.show()
sys.exit(app.exec())

