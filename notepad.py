from PySide6.QtWidgets import QWidget, QTextEdit, QVBoxLayout

class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        editor = QTextEdit()
        layout.addWidget(editor)
        self.setLayout(layout)
        self.setWindowTitle("Notepad — Windows 13")
