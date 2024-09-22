import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon


# QLabel
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar

class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.setWindowTitle("ilk pencerem")
        self.setGeometry(200, 300, 500, 400)  ## x, y , w, h
        self.setWindowIcon(QIcon("images/blue.ico"))
        self.setToolTip("bu bir deneme uygulamadır")

        self.initUI()

    def initUI(self) :
        self.lbl_name = QtWidgets.QLabel(self)
        self.lbl_name.setText("Adınız : ")
        self.lbl_name.move(30, 30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText("Soyadınız : ")
        self.lbl_surname.move(30, 70)

        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(100, 30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(100, 70)    

        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText("Kaydet")
        self.btn_save.move(100, 130)
        self.btn_save.clicked.connect(self.tikla)

        self.lbl_mesaj = QtWidgets.QLabel(self)
        self.lbl_mesaj.move(100, 150)
        self.lbl_mesaj.resize(300, 32)

    def tikla(self) :
        print(f"{self.txt_name.text()} - {self.txt_surname.text()}")
        self.lbl_mesaj.setText(f"{self.txt_name.text()} - {self.txt_surname.text()}")







if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


