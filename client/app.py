from PySide6.QtWidgets import QApplication
from controllers.chat1 import ChatWindow
import sys

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()

    window.show()
    app.exec_()