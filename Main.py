from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel
import sys

from Controller.Gamecontroller import Gamecontroller
from GUI.mainview import Window


def main():
    gamecontroller = Gamecontroller()
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
