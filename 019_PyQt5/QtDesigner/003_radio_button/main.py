import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  ## tanımlanan herşeye burdan erişilebilir
        self.ui.setupUi(self)

        self.ui.rb_turkiye.setChecked(True)  ## default seçim
        self.ui.rb_lise.setChecked(True) ## default seçim

        self.ui.btn_egitim.clicked.connect(self.egitim_sec)
        self.ui.btn_ulke.clicked.connect(self.ulke_sec)

        self.ui.rb_lise.toggled.connect(self.radyo_secim)
        self.ui.rb_universite.toggled.connect(self.radyo_secim)
        self.ui.rb_ilkokul.toggled.connect(self.radyo_secim)
        self.ui.rb_yukseklisans.toggled.connect(self.radyo_secim)



    def egitim_sec(self) :
        rbuttons = self.ui.gbox_egitim.findChildren(QRadioButton)
        for i in rbuttons :
            if i.isChecked() :
                self.ui.lbl_egitim.setText(i.text())

    def ulke_sec(self) :
        rbuttons = self.ui.gbox_ulke.findChildren(QRadioButton)
        for i in rbuttons :
            if i.isChecked() :
                self.ui.lbl_ulke.setText(i.text())

    # def radyo_secim(self) : ## boyle çalışır
    def radyo_secim(self, val) :  # val True-False değeri döndürür
        radio_btn = self.sender()
        print(f"{radio_btn.text()} - {val}")

    

    



        


    




if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
