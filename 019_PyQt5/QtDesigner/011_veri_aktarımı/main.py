import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from doktor import Ui_MainWindow 
from hasta_page import HastaPage 




class DoktorPage(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.hastaPage = HastaPage()
        self.hastaPage.show()
       

        self.hastaPage.hasta_sinyali.connect(self.hastaden_gelen_mesaj)
        self.ui.pushButton.clicked.connect(self.hastaya_giden_mesaj)
    
    def hastaden_gelen_mesaj(self, mesaj) :
        self.ui.label.setText(mesaj)
    
    def hastaya_giden_mesaj(self) :
        mesaj = self.ui.textEdit.toPlainText()
        self.hastaPage.ui.label.setText(mesaj)


   





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = DoktorPage()
    win.show()
    sys.exit(app.exec_())
