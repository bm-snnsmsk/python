from PyQt5 import QtWidgets
import sys
from combobox import Ui_MainWindow



class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # liste = ["adana","van"]
        # self.ui.cbox_sehirler.addItem("İstanbul")
        # self.ui.cbox_sehirler.addItems(liste)
        # self.ui.cbox_sehirler.addItems(["muş","bitlis"])

        self.ui.btn_sehir_ekle.clicked.connect(self.sehir_ekle)
        self.ui.btn_sehir_sec.clicked.connect(self.sehir_sec)
        self.ui.btn_sehir_temizle.clicked.connect(self.sehir_temizle)

        self.ui.cbox_sehirler.currentIndexChanged.connect(self.selectedChangedIndex)
        self.ui.cbox_sehirler.currentIndexChanged[str].connect(self.selectedChangedText)

      

        

    def selectedChangedText(self, text) : ## text = seçilen elemanın text bilgisi
        print(text)

    def selectedChangedIndex(self, index) : ## index = seçilen elemanın index bilgisi
        print(index)

    def sehir_ekle(self) :
        sehirler = ["adana","van","muş","bitlis","hakkari"]
        self.ui.cbox_sehirler.addItems(sehirler)

    def sehir_sec(self) :
        print(self.ui.cbox_sehirler.currentText())
        print(self.ui.cbox_sehirler.currentIndex())
        print(self.ui.cbox_sehirler.count())  ## toplam liste elemnı

        for i in range(self.ui.cbox_sehirler.count()) :
            print(self.ui.cbox_sehirler.itemText(i))

    def sehir_temizle(self) :        
        self.ui.cbox_sehirler.clear()


    

       


        
def app() :
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())  
    

app()


