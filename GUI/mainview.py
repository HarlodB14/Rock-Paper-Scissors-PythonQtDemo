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
        self.setWindowTitle("Rock Paper Scissors! - Harlod Bombala")
        self.setFixedSize(400, 500)
        self.gamecontroller = Gamecontroller()

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

        self.name_label = QLabel("")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.name_label)

        self.move_label = QLabel("")
        self.move_label.setAlignment(Qt.AlignCenter)
        self.move_label.hide()
        self.layout.addWidget(self.move_label)

        self.rps_buttons = []
        for move in self.gamecontroller.get_moves():
            btn = QPushButton(move)
            btn.clicked.connect(lambda _, m=move: self.player_makes_move(m))
            btn.hide()
            self.rps_buttons.append(btn)
            self.layout.addWidget(btn)

    def setup_game(self):
        name = self.name_input.text()
        if name:
            self.gamecontroller.set_player(name)
            self.name_label.setText(f"Welkom, {self.gamecontroller.getplayer().name}!")

            self.name_input.hide()
            self.name_button.hide()
            self.image_label.hide()
            self.name_label.setText("Kies een zet")
            self.name_label.show()
            for btn in self.rps_buttons:
                btn.show()

    def player_makes_move(self, move):
        self.gamecontroller.set_player_move(move)

        self.name_label.hide()
        for btn in self.rps_buttons:
            btn.hide()

        self.move_label.setText(f"Je koos: {move}")
        self.move_label.show()

        self.move_label.setText("AI kiest...")
        QTimer.singleShot(1000, self.show_winner)

    def show_winner(self):
        player_move = self.gamecontroller.get_player_move()
        ai_move = self.gamecontroller.get_ai_move()
        winner = self.gamecontroller.determine_winner(player_move, ai_move)

        if winner == "player":
            winner_name = self.gamecontroller.getplayer().name
        elif winner == "ai":
            winner_name = "AI"
        else:
            winner_name = "Gelijkspel"

        self.move_label.hide()
        self.name_label.hide()
        self.image_label.hide()

        if hasattr(self, 'win_screen'):
            self.win_screen.close()

        self.win_screen = WinScreen(winner_name, player_move, ai_move, self)
        self.win_screen.restart_signal.connect(self.restart_game)
        self.win_screen.show()

    def restart_game(self):
        self.gamecontroller = Gamecontroller()
        self.init_ui()
        self.image_label.show()
        self.name_input.show()
        self.name_button.show()
        self.name_label.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
