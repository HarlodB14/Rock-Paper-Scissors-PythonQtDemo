from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from Controller.Gamecontroller import Gamecontroller


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gamecontroller = Gamecontroller()
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle("Rock Paper Scissors! - Harlod Bombala")

        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Voer je naam in...")
        self.name_input.setGeometry(100, 50, 200, 30)

        self.name_button = QPushButton("Start spel", self)
        self.name_button.setGeometry(150, 90, 100, 30)
        self.name_button.clicked.connect(self.set_player_name)
        self.name_label = QLabel(self)
        self.name_label.setGeometry(100, 140, 200, 30)

    def set_player_name(self):
        name = self.name_input.text()
        if name:
            self.gamecontroller.set_player(name)
            self.name_label.setText(f"Welkom, {self.gamecontroller.getplayer().name}!")
            self.name_input.hide()
            self.name_button.hide()
