import sys

from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

import ws


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('design.ui', self)

        self.onSearch()

    def onSearch(self):
        weather = ws.get_weather(self.query.text())
        if weather:
            icon = QPixmap()
            icon.loadFromData(weather['icon'])
            self.icon.setPixmap(icon)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
