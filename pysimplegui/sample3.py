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
        label1 = QLabel('Voltage %02.3f V'%(c.voltage()))
        label1.setAlignment(Qt.AlignLeft)
        font1 = label1.font()
        font1.setPointSize(10)

        label1.setFont(font1)
        layout=QVBoxLayout()
        layout.addWidget(label1)

        self.setLayout(layout)

        self.move(300,300)
        self.resize(400,200)
        self.show()


if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

