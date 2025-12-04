from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt, QTimer

class BootScreen(QWidget):
    def __init__(self, proceed):
        super().__init__()
        self.proceed = proceed
        layout = QVBoxLayout()
        label = QLabel("Windows 13 — 128-bit OS Simulation\nBooting Kernel...")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        self.setLayout(layout)

        QTimer.singleShot(2000, self.finish_boot)

    def finish_boot(self):
        self.proceed()
