import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QMessageBox, QInputDialog, QLineEdit, QTableWidgetItem
from PyQt5.QtCore import QDate, QTime, QDateTime

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        # super(MainWindow, self).__init__() 
        super().__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)


       

        self.loadProducts()
        self.ui.btn_kaydet.clicked.connect(self.saveProduct)
        
        # self.ui.tableWidget.clicked.connect(self.tekClick)
        self.ui.tableWidget.doubleClicked.connect(self.doubleClick)

        ## çeşitli auayarlamalar ve metotlar
        # self.ui.tableWidget.setColumnWidth(0,100)
        # self.ui.tableWidget.setColumnWidth(1,250)    
        # secili_satır = self.ui.tableWidget.currentRow()
        # secili_id = self.ui.tableWidget.item(secili_satır, colon_numarasi)
        # secili_id = self.ui.tableWidget.item(secili_satır, colon_numarasi).text()   ## seçili satır numarası döndürür

       

    def doubleClick(self):
        print(self.ui.tableWidget.selectedItems())
        for item in self.ui.tableWidget.selectedItems():            
            print(item.row(), item.column(), item.text())    



    def saveProduct(self):
        name = self.ui.txt_name.text()
        price = self.ui.txt_price.text()

        if name and price is not None:
            rowCount = self.ui.tableWidget.rowCount()
            print(rowCount) ##▲ son sırayı bul 
            self.ui.tableWidget.insertRow(rowCount) ## son sıraya ekle
            self.ui.tableWidget.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableWidget.setItem(rowCount,1, QTableWidgetItem(price))

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
