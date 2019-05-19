import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

app = QApplication(sys.argv)

w = QWidget()
w.setGeometry(50, 50, 500, 500)
w.setWindowTitle('My First GUI')
w.setWindowIcon(QIcon('Icons/icon.png'))
w.show()

sys.exit(app.exec_())
