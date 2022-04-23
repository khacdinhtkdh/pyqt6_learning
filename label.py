import sys

from PyQt6.QtGui import QFont, QPixmap, QMovie
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

        label2 = QLabel(self)
        pixmap = QPixmap('image/image.png')
        label2.setPixmap(pixmap)

        label3 = QLabel(self)
        movie = QMovie('image/giphy.gif')
        label3.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
windown = Main()
windown.show()
app.exec()

