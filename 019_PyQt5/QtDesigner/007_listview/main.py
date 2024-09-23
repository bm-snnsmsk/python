import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtCore import QDate, QTime, QDateTime

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)


        self.loadStudents()
        
        self.ui.btn_ekle.clicked.connect(self.addStudent)
        self.ui.btn_duzenle.clicked.connect(self.editStudent)
        self.ui.btn_sil.clicked.connect(self.removeStudent)
        self.ui.btn_yukari.clicked.connect(self.upStudent)
        self.ui.btn_asagi.clicked.connect(self.downStudent)
        self.ui.btn_sirala.clicked.connect(self.sortStudents)
        self.ui.btn_exit.clicked.connect(self.close)

    def loadStudents(self):
        self.ui.lw_ogrenciler.addItems(['Ahmet','Ali','Çınar'])
        self.ui.lw_ogrenciler.setCurrentRow(1) ## mevcut index

    def addStudent(self):
        currentIndex = self.ui.lw_ogrenciler.currentRow() ## o anki seçili sıra
        text, ok = QInputDialog.getText(self, "New Student", "Student Name")
        if ok and text is not None:
            self.ui.lw_ogrenciler.insertItem(currentIndex ,text)

    def editStudent(self):
        index = self.ui.lw_ogrenciler.currentRow()
        item = self.ui.lw_ogrenciler.item(index)

        if item is not None:
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)
    
    def removeStudent(self):
        index = self.ui.lw_ogrenciler.currentRow()
        item = self.ui.lw_ogrenciler.item(index)
        
        if item is None:
            return

        q = QMessageBox.question(self, "Remove Student", "Do you want to remove student: " + item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            item = self.ui.lw_ogrenciler.takeItem(index)
            del item

    def upStudent(self):
        index = self.ui.lw_ogrenciler.currentRow()
        if index >= 1: ## seçili eleman en üstteki eleman değilse
            item = self.ui.lw_ogrenciler.takeItem(index)
            self.ui.lw_ogrenciler.insertItem(index-1, item)
            self.ui.lw_ogrenciler.setCurrentItem(item)

    def downStudent(self):
        index = self.ui.lw_ogrenciler.currentRow()
        if index < self.ui.lw_ogrenciler.count() -1 :## seçili eleman en alttaki eleman değilse
            item = self.ui.lw_ogrenciler.takeItem(index)
            self.ui.lw_ogrenciler.insertItem(index+1, item)
            self.ui.lw_ogrenciler.setCurrentItem(item)

    def sortStudents(self):
        self.ui.lw_ogrenciler.sortItems()

    def close(self):
        quit()

      
      


      

   





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
