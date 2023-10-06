from PyQt6.QtWidgets import QMainWindow, QLabel
from PyQt6 import QtCore


class HomeView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Home View")
        # Create a QLabel widget to display "Hello, World!"
        hello_label = QLabel("Hello, World!", self)
        hello_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        hello_label.setStyleSheet("font-size: 24px;")
        # Set the central widget to the QLabel
        self.setCentralWidget(hello_label)