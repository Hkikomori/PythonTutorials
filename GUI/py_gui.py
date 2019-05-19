import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5 import QtCore

class Fenster(QWidget):
    def __init__(self):
        super().__init__()
        self.initMe()

    def initMe(self):
        self.setGeometry(50, 50, 500, 500)
        self.setWindowTitle('My First GUI')
        self.setWindowIcon(QIcon('Icons/icon.png'))

        button = QPushButton('Click Me !',self)
        button.move(50,50)
        QToolTip.setFont(QFont('Arial', 8))
        button.setToolTip('<b>Nothing</b> will happen')
        button.clicked.connect(self.button_pressed)

        quit = QPushButton('Exit',self)
        quit.move(200,200)
        quit.setToolTip('Exit GUI')
        quit.clicked.connect(self.button_exit)

        self.show()

    def button_pressed(self):
        print('Hello World!')

    def button_exit(self):
        btn = self.sender()
        print('Exiting GUI')
        #QtCore.QCoreApplication.instance().quit



app = QApplication(sys.argv)
w = Fenster()
sys.exit(app.exec_())
