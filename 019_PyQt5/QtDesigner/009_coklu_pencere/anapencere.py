from PyQt5.QtWidgets import *
from anapencere_python import Ui_MainWindow
from urun_listele import UrunListelePage
from urun_kategori import UrunKategoriPage


class AnapencerePage(QMainWindow) :
    def __init__(self) :
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.urunListelePage = UrunListelePage()
        self.urunKategoriPage = UrunKategoriPage()

        self.ui.urunlistele.triggered.connect(self.urun_listele_formu)
        self.ui.kategoriEkle.triggered.connect(self.urun_kategori_ekle)

    def urun_listele_formu(self) :
        self.urunListelePage.show()
        
    def urun_kategori_ekle(self) :
        self.urunKategoriPage.show()

        