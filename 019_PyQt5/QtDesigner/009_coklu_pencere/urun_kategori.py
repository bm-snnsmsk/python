from PyQt5.QtWidgets import *
from urun_kategori_python import Ui_Form

# class UrunKategoriPage(QMainWindow) :
class UrunKategoriPage(QWidget) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        