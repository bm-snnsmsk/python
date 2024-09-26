import sys
from PyQt5.QtWidgets import QMainWindow, QApplication

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.ui.pushButton_artir.clicked.connect(self.artir)
        self.ui.pushButton_eksi.clicked.connect(self.azalt)
        self.ui.pushButton_sil.clicked.connect(self.sil)

        self.number = 0

    def artir(self) :
        self.number += 1
        self.ui.label_sonuc.setText(str(self.number))

    def azalt(self) :
        self.number -= 1
        self.ui.label_sonuc.setText(str(self.number))

       
    def sil(self) :
        # self.ui.label_sonuc.setText("")
        self.ui.label_sonuc.clear()

       
       



        


    




if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
