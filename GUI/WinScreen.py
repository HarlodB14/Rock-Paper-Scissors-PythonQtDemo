from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QPushButton, QWidget


class WinScreen(QWidget):
    restart_signal = QtCore.pyqtSignal()

    def __init__(self, winner_name, player_move, ai_move, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Resultaat")
        self.setFixedSize(300, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        moves_label = QLabel(f"Jij: {player_move}\nAI: {ai_move}")
        moves_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(moves_label)

        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.image_label)

        if winner_name == "AI":
            pixmap = QPixmap("../Resources/Images/images.jpg")
            result_text = "AI heeft gewonnen!"
        elif winner_name == "Tie":
            pixmap = QPixmap("../Resources/Images/download.jpg")
            result_text = "Het is een gelijkspel!"
        elif winner_name == "Player":
            pixmap = QPixmap("../Resources/Images/img_1.png")
            result_text = "Jij hebt gewonnen!"
        else:
            pixmap = QPixmap()
            result_text = "Onbekende uitkomst"

        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            self.image_label.setPixmap(scaled_pixmap)

        winner_label = QLabel(result_text)
        winner_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(winner_label)

        self.restart_btn = QPushButton("Opnieuw spelen")
        self.restart_btn.clicked.connect(self.handle_restart)
        layout.addWidget(self.restart_btn)

    def handle_restart(self):
        self.restart_signal.emit()
        self.close()
