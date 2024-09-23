import sys
from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QRadioButton, QMessageBox

from untitled import Ui_MainWindow


class MainWindow(QMainWindow) :
    def __init__(self) :
        super(MainWindow, self).__init__() 
        self.ui = Ui_MainWindow()  
        self.ui.setupUi(self)

        self.ui.btn_exit.clicked.connect(self.show_dialog)

    
    def show_dialog(self) :

        ################ kısa gösterim STAR ##############
        result = QMessageBox().question(self, "başlık", "mesajjjj", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Cancel)
        if result == QMessageBox.Ok :
            print("ok tuşuna basıldı")
            QtWidgets.qApp.quit()
        elif result == QMessageBox.Cancel :
            print("cancel tuşuna basıldı...")
        ######## uzun gösterim  END #####################

        ######## uzun gösterim  START ###################
        # mesaj = QMessageBox()
        # mesaj.setWindowTitle("Mesaj başlığı")
        # mesaj.setText("Çıkış yapmak istediğinize emin misiniz?")

        # mesaj.setIcon(QMessageBox.Question)
        # mesaj.setIcon(QMessageBox.Information)
        # mesaj.setIcon(QMessageBox.Warning)

        # mesaj.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # mesaj.setDefaultButton(QMessageBox.Ok)
        # mesaj.setDefaultButton(QMessageBox.Cancel)
        # mesaj.setDetailedText("Detaylar burda....")

        # mesaj.buttonClicked.connect(self.popup_btn)

        # x = mesaj.exec_()

        # print(x)
    
    # def popup_btn(self, i) :
    #     # print(i.text())

    #     if i.text() == "OK" :
    #         print("OK tuşuna basıldı")
    #         QtWidgets.qApp.quit()  ## uygulama kapatır

    #     elif i.text() == "Cancel" :
    #         print("Cancel tuşuna basıldı")

    #     elif i.text() == "Ignore" :
    #         print("Ignore tuşuna basıldı")
    ######## uzun gösterim  END #####################





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
