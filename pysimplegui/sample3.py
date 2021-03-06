import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from ina260.controller import Controller


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My First Application')
        self.setWindowIcon(QIcon('leehands.png'))

        c = Controller(address=0x45)
        #volt = "%02.3f V"
        self.qLbl = QLabel('Not Yet Init')
        self.setCentralWidget(self.qLbl)

        self.move(300,300)
        self.resize(400,200)
        self.show()
    def update(self):
        self.qLbl.setText('Votage : %02.3fV' %(c.voltage()))
    def run(self):
        self.app.exec_()
        


if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

