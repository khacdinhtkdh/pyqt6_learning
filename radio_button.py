import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie, QIcon
from PyQt6.QtWidgets import *


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.lb = None
        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("Pyqt 6")

        self.create_widget()

    def create_widget(self):
        hbox = QHBoxLayout()

        self.lb = QLabel("Hello")

        rd_btn = QRadioButton('Python')
        rd_btn.setIcon(QIcon('image/icon.png'))
        # rd_btn.setChecked(True)
        rd_btn.toggled.connect(self.radio_selected)

        rd_btn2 = QRadioButton('Java')
        rd_btn2.setIcon(QIcon('image/icon.png'))
        # rd_btn2.setChecked(True)
        rd_btn2.toggled.connect(self.radio_selected)

        rd_btn3 = QRadioButton('JavaScript')
        rd_btn3.setIcon(QIcon('image/icon.png'))
        # rd_btn3.setChecked(True)
        rd_btn3.toggled.connect(self.radio_selected)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lb)
        vbox.addLayout(hbox)

        hbox.addWidget(rd_btn)
        hbox.addWidget(rd_btn2)
        hbox.addWidget(rd_btn3)
        self.setLayout(vbox)

    def radio_selected(self):
        radio_btn = self.sender()
        if radio_btn.isChecked():
            self.lb.setText('you have selected: {}'.format(radio_btn.text()))



app = QApplication(sys.argv)
windown = Main()
windown.show()
sys.exit(app.exec())

