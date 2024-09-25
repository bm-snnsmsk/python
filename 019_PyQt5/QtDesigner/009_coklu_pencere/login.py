from PyQt5.QtWidgets import *
from login_python import Ui_Form
from anapencere import AnapencerePage


class LoginPage(QWidget) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.anapencerePage = AnapencerePage()
        self.ui.pushButton.clicked.connect(self.giris_yap)


    def giris_yap(self):
        username = self.ui.lineEdit_kullaniciadi.text()
        sifre = self.ui.lineEdit_sifre.text()
        if username == "snn" and sifre == "123" :
            # self.hide()
            self.close()
            self.anapencerePage.show()
            
            
