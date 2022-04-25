import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = None
        self.setGeometry(200, 200, 400, 300)
        self.setWindowTitle("Pyqt 6")

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()

        self.lb = QLabel("")
        self.check_book1 = QCheckBox('Python')
        self.check_book2 = QCheckBox('Java')
        self.check_book3 = QCheckBox('JS')
        self.check_book1.stateChanged.connect(self.checkbook_selected)
        self.check_book2.stateChanged.connect(self.checkbook_selected)
        self.check_book3.stateChanged.connect(self.checkbook_selected)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)

        hbox.addWidget(self.check_book1)
        hbox.addWidget(self.check_book2)
        hbox.addWidget(self.check_book3)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def checkbook_selected(self):
        value = ""

        if self.check_book1.isChecked():
            value += self.check_book1.text()
        if self.check_book2.isChecked():
            value += self.check_book2.text()
        if self.check_book3.isChecked():
            value += self.check_book3.text()

        self.lb.setText("Selected: {}".format(value))



app = QApplication(sys.argv)
windown = Main()
windown.show()
sys.exit(app.exec())

