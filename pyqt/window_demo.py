"""
Asim Code
Install PyQt5 and Create an Empty Window in Python
https://youtu.be/4jHTOdxik70
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget

class DemoWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle('PyQt5 Demo Window')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoWindow()
    sys.exit(app.exec_())
