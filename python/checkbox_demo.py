import sys
from PyQt5.QTWidgets import (QApplication, QWidget, QCheckBox, Qlabel)
from PyQt5.QtCore import QtCore
class CreateCheckBoxWindow(Qwidget):
    def __int__(self):
        super().__init__()
        self.initWindow()
    def initWindow(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle('QCheckBox Example')
        self.showCheckBoxes()
        self.show()
    def showCheckBoxes(self):
        head_label = QLabel(self)
        head_label.setText("Which programming you like ?")
        head_label.setWordWrap(True)
        head_label.move(10,10)
        head_label.resize(230,60)
        python_programming = QCheckBox("Python")
        python_programming.move(20,80)
        python_programming.stateChanged.connect(self.printInfo)

        java_programming = QCheckBox("Java")
        python_programming.move(20,120)
        python_programming.stateChanged.connect(self.printInfo)
    def printInfo(self,state):
        sender = self.sender()
        if state == Qt.Checked:
            print("{} selected.".format(sender.text()))
        else:
            print("{} Deselected.".format(sender.text()))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CreateCheckBoxWindow() 
    sys.exit(app.exec_())   
        
