import sys
from random import randint

from PyQt6 import QtWidgets
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow

from ui_form import Ui_MainWindow


class YellowCircles(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.drawButton.clicked.connect(self.draw)

        self.circles: list[tuple[int, int, int]] = []

    def draw(self):
        self.circles = [
            (
                diameter := randint(10, 100),
                randint(0, self.width() - diameter),
                randint(0, self.height() - diameter)
            )
            for _ in range(randint(5, 30))]

        self.update()

    def paintEvent(self, event):
        drawer: QPainter = QPainter(self)

        for (diameter, x, y) in self.circles:
            drawer.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
            drawer.drawEllipse(x, y, diameter, diameter)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = YellowCircles()
    window.show()
    sys.exit(app.exec())
