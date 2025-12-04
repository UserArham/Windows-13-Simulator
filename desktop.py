from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap

class Desktop(QWidget):
    def __init__(self, syscall):
        super().__init__()
        self.syscall = syscall
        layout = QVBoxLayout()

        wallpaper = QLabel()
        wallpaper.setPixmap(QPixmap("assets/wallpaper.jpg"))
        wallpaper.setScaledContents(True)
        layout.addWidget(wallpaper)

        btn = QPushButton("Open Notepad")
        btn.clicked.connect(lambda: self.syscall.open_app("Notepad"))
        layout.addWidget(btn)

        self.setLayout(layout)
