import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, renk):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)  ## arkaplan rengi vermek için

        palet = self.palette() ## arkaplan rengi vermek için
        palet.setColor(QPalette.Window, QColor(renk)) ## arkaplan rengi vermek için
        self.setPalette(palet) ## arkaplan rengi vermek için

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Renk Çalışması")
        self.setGeometry(200, 200, 500, 500)  ## x, y , w, h

        widget = Color("blue")  ## arkaplan rengi vermek için
        self.setCentralWidget(widget) ## arkaplan rengi vermek için
        
        





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



