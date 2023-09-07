import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

ui = uic.loadUiType("custum.ui")[0]
#custum ui를 가지고 와서 적용

class Main(QMainWindow, ui):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)

app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()