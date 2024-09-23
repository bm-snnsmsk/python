import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)


        # self.ui.cbx_sehirler.addItem("Ankara")
        # self.ui.cbx_sehirler.addItem("Silopi")
        # self.ui.cbx_sehirler.addItem("Mardin")

        self.combo = self.ui.cbx_sehirler

        # self.liste = ["Silopi","şırnak","mardin","hakkari","urfa","istanbul"]
        # self.ui.cbx_sehirler.addItems(self.liste)

        self.ui.btn_getir.clicked.connect(self.verileri_yukle)
        self.ui.btn_yukleme.clicked.connect(self.verileri_getir)
        self.ui.btn_temizle.clicked.connect(self.verileri_temizle)

        self.ui.cbx_sehirler.currentIndexChanged.connect(self.selected_changed_index)  ## herhangi bir şey belirtilmezse index döndürür
        self.ui.cbx_sehirler.currentIndexChanged[str].connect(self.selected_changed_text) ## [str] parametresi verilirse text bilgisi döndürür

    def verileri_yukle(self) :
        sehirler = ["diyarbakır","adana","izmir","malatya","cizre","silopi","idil","nusaybin"]
        self.combo.addItems(sehirler)

    def verileri_getir(self) :
        print(f"{self.ui.cbx_sehirler.currentText()} - {self.ui.cbx_sehirler.currentIndex()} - {self.ui.cbx_sehirler.count()}")
        print("###################################")
        for i in range(self.ui.cbx_sehirler.count()) :
            print(self.ui.cbx_sehirler.itemText(i))

    def selected_changed_index(self, val) :
        print(f"seçilen index : {val}")

    def selected_changed_text(self, val) :
        print(f"seçilen text : {val}")

    def verileri_temizle(self) :
        self.combo.clear()

    

        




        


    



        


    




if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
