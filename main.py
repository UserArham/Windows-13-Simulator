from PySide6.QtWidgets import QApplication, QStackedWidget
from kernel.kernel128 import Kernel128
from kernel.syscalls import SysCall
from gui.boot_screen import BootScreen
from gui.desktop import Desktop
import sys

app = QApplication(sys.argv)

kernel = Kernel128()
syscall = SysCall(kernel)

stack = QStackedWidget()

def load_desktop():
    desktop = Desktop(syscall)
    stack.addWidget(desktop)
    stack.setCurrentWidget(desktop)

boot = BootScreen(load_desktop)
stack.addWidget(boot)
stack.setCurrentWidget(boot)

stack.show()
sys.exit(app.exec())
