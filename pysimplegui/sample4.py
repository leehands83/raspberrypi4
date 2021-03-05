import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer
from ina260.controller import Controller

c = Controller(address=0x45)

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setWindowTitle('Voltage Monitor')
        self.setWindowIcon(QIcon('leehands.png'))

        self.qLbl = QLabel('Not Yet Init')
        self.setCentralWidget(self.qLbl)
        self.resize(400,100)
        
        self.qTimer = QTimer()
        self.qTimer.setInterval(500)
        self.qTimer.timeout.connect(self.getSensorValue)
        self.qTimer.start()

    def getSensorValue(self):
        self.qLbl.setText('  Votage : %02.3fV \n  Current : %3.0fmA\n  Power   : %3.0fmW'
        %(c.voltage(),c.current()*1000,c.power()*1000))


qApp = QApplication(sys.argv)
qWin=MainWindow()
qWin.show()
sys.exit(qApp.exec_())
