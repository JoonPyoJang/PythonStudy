import sys
from PyQt5.QtWidgets import *

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(100,100, 800, 1000)
        self.setWindowTitle("워밍업 프로그램")

        # 시세조회
        self.getPriceLabel = QLabel("현재가격", self)
        self.getPriceTextEdit = QTextEdit(self)
        self.getPriceTextEdit.move(0, 30)
        self.getPriceButton = QPushButton("조회", self)
        self.getPriceButton.move(120, 30)

        # 매수
        self.buyPriceLabel = QLabel("매수 금액", self)
        self.buyPriceLabel.move(0, 60)
        self.buyPriceTextEdit = QTextEdit(self)
        self.buyPriceTextEdit.move(0, 90)
        self.buyPriceButton = QPushButton("매수", self)
        self.buyPriceButton.move(120, 120)

        # 매도도
        self.sellPriceLabel = QLabel("매도금액", self)
        self.sellPriceLabel.move(0, 150)
        self.sellPriceTextEdit = QTextEdit(self)
        self.sellPriceTextEdit.move(0, 180)
        self.sellPriceButton = QPushButton("조회", self)
        self.sellPriceButton.move(120, 210)



app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()