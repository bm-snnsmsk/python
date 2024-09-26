import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QMessageBox, QInputDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import QDate, QTime, QDateTime
import json

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        # super(MainWindow, self).__init__() 
        super().__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)


        self.loadProducts()

        self.ui.btn_kaydet.clicked.connect(self.saveProduct)
        self.ui.pushButton_sil.clicked.connect(self.satir_sil)
        self.ui.pushButton_verileri_getir.clicked.connect(self.loadProducts)
        self.ui.pushButton_sutun_ekle.clicked.connect(self.sutun_ekle)
        
        
        # self.ui.tableWidget.clicked.connect(self.tekClick)
        # self.ui.tableWidget.doubleClicked.connect(self.doubleClick)
        self.ui.tableWidget.cellChanged.connect(self.icerik_degisti)

        ## çeşitli auayarlamalar ve metotlar
        # self.ui.tableWidget.setColumnWidth(0,100)
        # self.ui.tableWidget.setColumnWidth(1,250)    
        # secili_satır_indexi = self.ui.tableWidget.currentRow()       
        # secili_id = self.ui.tableWidget.item(secili_satır, colon_numarasi).text()   ## seçili satır numarası döndürür

    def satir_sil(self):
        secili_satir = self.ui.tableWidget.currentRow()
        self.ui.tableWidget.removeRow(secili_satir)
        print(f"{secili_satir} numaraslı satır silindi..")


    def sutun_ekle(self):
        secili_sutun = self.ui.tableWidget.currentColumn()
        sutun_sayisi = self.ui.tableWidget.columnCount()
        self.ui.tableWidget.insertColumn(sutun_sayisi)
        print(sutun_sayisi)


    def icerik_degisti(self) :
        secili_satir_item = self.ui.tableWidget.currentItem().text()
        secili_satir_indexi = self.ui.tableWidget.currentRow() 
        secili_satir_kolon = self.ui.tableWidget.currentColumn()
        # print(secili_satir_item)
        id = self.ui.tableWidget.item(secili_satir_indexi, 0).text()  ## video örneğinde id 0. kolonda olduğu için böyle bir yol izlendi
        print(f"id : {id} - kolon : {secili_satir_kolon} - satir : {secili_satir_indexi} - değer : {secili_satir_item}")
       

    def doubleClick(self):
        print(self.ui.tableWidget.selectedItems())
        for item in self.ui.tableWidget.selectedItems():            
            print(item.row(), item.column(), item.text())    

    def tekClick(self):
        secili_satir_indexi = self.ui.tableWidget.currentRow() 
        print(f"secili_satır_indexi : {secili_satir_indexi}") 




    def saveProduct(self):
        name = self.ui.txt_name.text()
        price = self.ui.txt_price.text()

        if name and price is not None:
            rowCount = self.ui.tableWidget.rowCount()
            # print(rowCount) ##▲ son sırayı bul 
            self.ui.tableWidget.insertRow(rowCount) ## son sıraya satır ekle
            self.ui.tableWidget.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(rowCount,1, QTableWidgetItem(price))
        
        # with open("urunler.json" ,"a") as f :
        #     json.dump(person, f)

    def loadProducts(self):

        products = [
            {'name': 'Samsung S5', 'price': 2000},
            {'name': 'Samsung S6', 'price': 3000},
            {'name': 'Samsung S7', 'price': 4000},
            {'name': 'Samsung S8', 'price': 5000}
        ]

        self.ui.tableWidget.setRowCount(len(products)) ## property editorden de ayalanabilir ama burda dinamik olmuş orda sabit kalır
        self.ui.tableWidget.setColumnCount(2) #

        self.ui.tableWidget.setHorizontalHeaderLabels(('ürün isim','fiyat'))
        self.ui.tableWidget.setColumnWidth(0,200)  ## kolon genişlik
        self.ui.tableWidget.setColumnWidth(1,100)

        rowIndex = 0
        for product in products:
            
            self.ui.tableWidget.setItem(rowIndex,0, QTableWidgetItem(product['name'])) ## satır, kolon, içerik
            self.ui.tableWidget.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))
            
            rowIndex+=1
        



      
      


      

   





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
