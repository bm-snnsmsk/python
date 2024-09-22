import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  ## tanımlanan herşeye burdan erişilebilir
        self.ui.setupUi(self)

        self.ui.cbx_sinema.stateChanged.connect(self.show_state)   
        self.ui.cbx_kitap.stateChanged.connect(self.show_state)
        self.ui.cbx_spor.stateChanged.connect(self.show_state)

        # self.ui.cb_defter.stateChanged.connect(self.show_state_2)
        # self.ui.cb_kalem.stateChanged.connect(self.show_state_2)
        # self.ui.cb_silgi.stateChanged.connect(self.show_state_2)

        self.ui.btn_secim.clicked.connect(self.get_all_secim)
        self.ui.btn_secim_2.clicked.connect(self.get_all_secim_2)

    
    def show_state(self, val) :  ## seciç true ise 2 , false ise 0
        # print(val) 
        # print(self.ui.cbx_sinema.isChecked()) 
        # print(self.ui.cbx_sinema.text()) 
        check_box = self.sender() ## hangi checkbox seçili
        
    
    def get_all_secim(self) :  
        result = ""
        # items = self.ui.centralwidget.findChildren(QCheckBox)  ## ana pencere üzerindeki tüm checkboxları getir
        items = self.ui.gbox_hobiler.findChildren(QCheckBox)  ## sadece gbox_hobiler üzerindeki checkboxları getir
        # print(items)
        for i in items :
            # print(i)
            if i.isChecked() == True :
                print(i.text())
                result += i.text() + "\n"
        self.ui.lbl_sonuc.setText(result)
        
    
    def get_all_secim_2(self) :  
        result = ""
        items = self.ui.gbox_kirtasiye.findChildren(QCheckBox)
        for i in items :
            if i.isChecked() == True :
                print(i.text())
                result += i.text() + "\n"
        self.ui.lbl_sonuc_2.setText(result)
        


    



        


    




if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
