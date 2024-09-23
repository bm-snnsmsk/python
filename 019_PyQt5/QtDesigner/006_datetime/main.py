import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QMessageBox
from PyQt5.QtCore import QDate, QTime, QDateTime

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.now = QDate.currentDate()


        self.ui.btn_tikla.clicked.connect(self.hesapla)

    def hesapla(self) :
        start = self.ui.dateEdit.date()
        end = self.ui.dateEdit_2.date()
        print(start, end)
        print(start.year())
        print(start.month())
        print(start.daysInMonth())
        print(start.daysInYear())
        # print(self.now)
        print(f"iki tarih arası toplam gün : {start.daysTo(end)} gün")
        print(f"iki tarih arası toplam gün : {start.daysTo(self.now)} gün")



      

   





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
