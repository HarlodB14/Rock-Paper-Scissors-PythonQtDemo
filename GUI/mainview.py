from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, QLineEdit, QPushButton, QLabel,
    QVBoxLayout, QWidget, QApplication
)
import sys

from Controller.Gamecontroller import Gamecontroller


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.move_label = None
        self.setWindowTitle("Rock Paper Scissors! - Harlod Bombala")
        self.setFixedSize(400, 500)
        self.gamecontroller = Gamecontroller()

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)
        central_widget.setLayout(self.layout)

        self.image_label = QLabel()
        pixmap = QPixmap("../Resources/Images/RPS.png")
        scaled_pixmap = pixmap.scaledToWidth(350)  # Schaal netjes
        self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Voer je naam in...")
        self.layout.addWidget(self.name_input)

        self.name_button = QPushButton("opslaan")
        self.name_button.clicked.connect(self.set_player_name)
        self.layout.addWidget(self.name_button)

        self.name_label = QLabel("")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.name_label)

        self.rps_buttons = []
        for move in self.gamecontroller.get_moves():
            btn = QPushButton(move)
            btn.clicked.connect(lambda _, m=move: self.player_makes_move(m))
            btn.hide()
            self.rps_buttons.append(btn)
            self.layout.addWidget(btn)

    def set_player_name(self):
        name = self.name_input.text()
        if name:
            self.gamecontroller.set_player(name)
            self.name_label.setText(f"Welkom, {self.gamecontroller.getplayer().name}!")
            self.name_input.hide()
            self.name_button.hide()

            for btn in self.rps_buttons:
                btn.show()

    def player_makes_move(self, move):
        self.gamecontroller.set_player_move(move)
        self.move_label.setText(f"je koos: {move}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
