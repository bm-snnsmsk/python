import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  ## tanımlanan herşeye burdan erişilebilir
        self.ui.setupUi(self)

        self.ui.btn_toplama.clicked.connect(self.hesaplama)
        self.ui.btn_cikarma.clicked.connect(self.hesaplama)
        self.ui.btn_carpma.clicked.connect(self.hesaplama)
        self.ui.btn_bolme.clicked.connect(self.hesaplama)

    def hesaplama(self):
        sender = self.sender().text()
        result = 0

        print(f"butonun texti : {sender}")
        if sender == '+':
            result = int(self.ui.txt_sayi1.text()) + int(self.ui.txt_sayi2.text())
        elif sender == '-':
            result = int(self.ui.txt_sayi1.text()) - int(self.ui.txt_sayi2.text())
        elif sender == 'x':
            result = int(self.ui.txt_sayi1.text()) * int(self.ui.txt_sayi2.text())
        elif sender == '/':
            result = int(self.ui.txt_sayi1.text()) / int(self.ui.txt_sayi2.text())

        self.ui.lbl_sonuc.setText('sonuç: '+ str(result))


    




if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
