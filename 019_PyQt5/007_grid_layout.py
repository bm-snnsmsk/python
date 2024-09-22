import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
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


        grid_layout = QGridLayout()


        grid_layout.addWidget(Color("orange"), 0 ,0)   ## row, column
        grid_layout.addWidget(Color("purple"), 0 ,1)    ## row, column
        grid_layout.addWidget(Color("lightgreen"), 0 ,2)  ## row, column
        grid_layout.addWidget(Color("red"), 1 ,0)   ## row, column
        grid_layout.addWidget(Color("blue"), 1 ,1)   ## row, column
        grid_layout.addWidget(Color("yellow"), 1 ,2)  ## row, column
        grid_layout.addWidget(Color("green"), 2 ,0)   ## row, column
        grid_layout.addWidget(Color("black"), 2 ,1)    ## row, column

        grid_layout.setContentsMargins(30, 75, 50, 30)  ## l - t - r - b 
        grid_layout.setSpacing(30)  ## 
 
        widget = QWidget()
        widget.setLayout(grid_layout)

        self.setCentralWidget(widget) 
        
        





if __name__ == '__main__' :
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())



