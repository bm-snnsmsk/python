from PyQt5.QtWidgets import *
from hasta import Ui_MainWindow 
from PyQt5.QtCore import pyqtSignal


class HastaPage(QMainWindow) :
    hasta_sinyali = pyqtSignal(str)
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.hasta_mesaj)

    def hasta_mesaj(self) :
        mesaj = self.ui.textEdit.toPlainText()  ## textEdit içeriği .text() ile değil toPlainText()
        self.hasta_sinyali.emit(mesaj)