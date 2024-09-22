import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

def MainWindow() :
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("ilk pencerem")
    win.setGeometry(200, 300, 1500, 500)  ## x, y , w, h
    win.setWindowIcon(QIcon("images/blue.ico"))
    win.setToolTip("bu bir deneme uygulamadır")

    win.show()
    sys.exit(app.exec_())


MainWindow()