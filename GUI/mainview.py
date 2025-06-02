from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QMainWindow, QLineEdit, QPushButton, QLabel,
    QVBoxLayout, QWidget, QApplication
)
import sys

from Controller.Gamecontroller import Gamecontroller
from GUI.WinScreen import WinScreen


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.move_image_label = None
        self.setWindowTitle("Rock Paper Scissors! - Harlod Bombala")
        self.setFixedSize(400, 500)
        self.gamecontroller = Gamecontroller()

        # Create labels here
        self.welcome_label = QLabel("")
        self.welcome_label.setAlignment(Qt.AlignCenter)

        self.name_label = QLabel("")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.hide()

        self.init_ui()

    def init_ui(self):
        if hasattr(self, 'central_widget'):
            self.central_widget.deleteLater()

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(15)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.central_widget.setLayout(self.layout)

        # Add widgets to layout AFTER layout is created
        self.layout.addWidget(self.welcome_label)
        self.layout.addWidget(self.name_label)

        self.image_label = QLabel()
        pixmap = QPixmap("../Resources/Images/RPS.png")
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaledToWidth(350)
            self.image_label.setPixmap(scaled_pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.image_label)

        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Give me your username...")
        self.layout.addWidget(self.name_input)

        self.name_button = QPushButton("Save")
        self.name_button.clicked.connect(self.setup_game)
        self.layout.addWidget(self.name_button)

        self.rps_buttons = []
        for move in self.gamecontroller.get_moves():
            btn = QPushButton(move)
            btn.clicked.connect(lambda _, m=move: self.player_makes_move(m))
            btn.hide()  # hide initially
            self.rps_buttons.append(btn)
            self.layout.addWidget(btn)

    def setup_game(self):
        name = self.name_input.text()
        if name:
            self.gamecontroller.set_player(name)
            self.welcome_label.setText(f"Welkom, {self.gamecontroller.getplayer().name}!")
            self.welcome_label.show()

            self.name_input.hide()
            self.name_button.hide()
            self.image_label.hide()
            self.name_label.setText("Kies een zet")
            self.name_label.show()

            self.create_move_image()

            for btn in self.rps_buttons:
                btn.show()

    def create_move_image(self):
        if self.move_image_label is not None:
            try:
                self.move_image_label.show()
                return
            except RuntimeError:
                self.move_image_label = None

        self.move_image_label = QLabel()
        move_pixmap = QPixmap("../Resources/Images/img_3.png")
        if not move_pixmap.isNull():
            scaled_pixmap = move_pixmap.scaledToWidth(350, Qt.SmoothTransformation)
            self.move_image_label.setPixmap(scaled_pixmap)
        self.move_image_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.move_image_label)

    def player_makes_move(self, move):
        self.gamecontroller.set_player_move(move)

        player_move = self.gamecontroller.get_player_move().capitalize()
        ai_move = self.gamecontroller.get_ai_move().capitalize()

        winner_name = self.gamecontroller.determine_winner(player_move, ai_move)

        # pass moves and winner to WinScreen
        self.win_screen = WinScreen(winner_name, player_move, ai_move)
        self.win_screen.restart_signal.connect(self.restart_game)
        self.win_screen.show()

    def show_winner(self):
        winner_key = self.gamecontroller.get_winner_name()

        winner_display_map = {
            "player": "Player",
            "ai": "AI",
            "tie": "Gelijkspel"
        }
        winner_name = winner_display_map.get(winner_key, "Gelijkspel")

        player_move = self.gamecontroller.get_player_move()
        ai_move = self.gamecontroller.get_ai_move()

        self.win_screen = WinScreen(winner_name, player_move, ai_move)
        self.win_screen.restart_signal.connect(self.restart_game)
        self.win_screen.show()

    def restart_game(self):
        self.gamecontroller = Gamecontroller()
        self.init_ui()
        self.image_label.show()
        self.name_input.show()
        self.name_button.show()
        self.welcome_label.setText("")
        self.name_label.setText("")
        self.name_label.hide()
        self.welcome_label.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
