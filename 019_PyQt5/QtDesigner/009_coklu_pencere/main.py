from PyQt5.QtWidgets import QApplication
from login import LoginPage


app = QApplication([])
win = LoginPage()
win.show()
app.exec_()
