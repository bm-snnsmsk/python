import sys
from PyQt5 import QtWidgets
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


def MainWindow() :


    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle("ilk pencerem")
    win.setGeometry(200, 300, 500, 400)  ## x, y , w, h
    win.setWindowIcon(QIcon("images/blue.ico"))
    win.setToolTip("bu bir deneme uygulamadır")

    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText("Adınız : ")
    lbl_name.move(30, 30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText("Soyadınız : ")
    lbl_surname.move(30, 70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(100, 30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(100, 70)
    

    def tikla(self) :
        print(f"{txt_name.text()} - {txt_surname.text()}")
    
    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText("Kaydet")
    btn_save.move(100, 130)
    btn_save.clicked.connect(tikla)

    win.show()
    sys.exit(app.exec_())

# def tikla() :
#     print("tıklanma başarılı")


MainWindow()