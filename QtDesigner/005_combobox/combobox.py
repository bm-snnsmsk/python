# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combobox.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 598)
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cbox_sehirler = QtWidgets.QComboBox(self.centralwidget)
        self.cbox_sehirler.setGeometry(QtCore.QRect(70, 80, 200, 50))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.cbox_sehirler.setFont(font)
        self.cbox_sehirler.setObjectName("cbox_sehirler")
        self.cbox_sehirler.addItem("")
        self.cbox_sehirler.addItem("")
        self.cbox_sehirler.addItem("")
        self.cbox_sehirler.addItem("")
        self.cbox_sehirler.addItem("")
        self.cbox_sehirler.addItem("")
        self.cbox_sehirler.addItem("")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(340, 80, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_sonuc.setFont(font)
        self.lbl_sonuc.setText("")
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        self.btn_sehir_sec = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sehir_sec.setGeometry(QtCore.QRect(70, 210, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_sehir_sec.setFont(font)
        self.btn_sehir_sec.setObjectName("btn_sehir_sec")
        self.btn_sehir_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sehir_ekle.setGeometry(QtCore.QRect(330, 210, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_sehir_ekle.setFont(font)
        self.btn_sehir_ekle.setObjectName("btn_sehir_ekle")
        self.btn_sehir_temizle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sehir_temizle.setGeometry(QtCore.QRect(580, 210, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.btn_sehir_temizle.setFont(font)
        self.btn_sehir_temizle.setObjectName("btn_sehir_temizle")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 43))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cbox_sehirler.setCurrentText(_translate("MainWindow", "Ağrı"))
        self.cbox_sehirler.setItemText(0, _translate("MainWindow", "Ağrı"))
        self.cbox_sehirler.setItemText(1, _translate("MainWindow", "Diyarbakır"))
        self.cbox_sehirler.setItemText(2, _translate("MainWindow", "Gaziantep"))
        self.cbox_sehirler.setItemText(3, _translate("MainWindow", "Mardin"))
        self.cbox_sehirler.setItemText(4, _translate("MainWindow", "Siirt"))
        self.cbox_sehirler.setItemText(5, _translate("MainWindow", "Şanlıurfa"))
        self.cbox_sehirler.setItemText(6, _translate("MainWindow", "Şırnak"))
        self.btn_sehir_sec.setText(_translate("MainWindow", "Get İtem"))
        self.btn_sehir_ekle.setText(_translate("MainWindow", "Şehir Ekle"))
        self.btn_sehir_temizle.setText(_translate("MainWindow", "Temizle"))