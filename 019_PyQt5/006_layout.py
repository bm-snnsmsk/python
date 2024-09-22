import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPalette, QColor

class Color(QWidget):
    def __init__(self, renk):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)  

        palet = self.palette() 
        palet.setColor(QPalette.Window, QColor(renk)) 
        self.setPalette(palet) 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Renk Çalışması")
        self.setGeometry(200, 200, 500, 500)  ## x, y , w, h



        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout_2 = QHBoxLayout()


        horizontal_layout_2.addWidget(Color("orange"))
        horizontal_layout_2.addWidget(Color("purple"))
        horizontal_layout_2.addWidget(Color("lightgreen"))

        horizontal_layout.addWidget(Color("red"))
        horizontal_layout.addWidget(Color("blue"))
        horizontal_layout.addWidget(Color("yellow"))
        horizontal_layout.addWidget(Color("green"))
        horizontal_layout.addWidget(Color("black"))

        vertical_layout.addWidget(Color("pink"))
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addLayout(horizontal_layout_2)
        vertical_layout.addWidget(Color("lightblue"))


        widget = QWidget()
        widget.setLayout(vertical_layout)

        self.setCentralWidget(widget) 
        
        





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



