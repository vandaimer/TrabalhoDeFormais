# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from Automaton import Automaton
from FiniteAutomaton import FiniteAutomaton
from RegularExpression import RegularExpression
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        self.AFND = Automaton()
        self.AFD = FiniteAutomaton()
        self.RegEx = RegularExpression()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 470, 531, 28))
        self.lineEdit.setText("")
        self.lineEdit.setFrame(True)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(130, 500, 151, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 500, 141, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(455, 20, 311, 371))
        self.tableView.setObjectName("tableView")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(272, 70, 161, 28))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(104, 70, 151, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 500, 201, 28))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2.clicked.connect(self.salva_regex)##ADICIONA ACTION

        self.pushButton.clicked.connect(self.carrega_regex)##ADICIONA ACTION

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 110, 121, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(290, 150, 121, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 190, 121, 28))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(190, 110, 85, 28))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(190, 150, 85, 28))
        self.pushButton_8.setObjectName("pushButton_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "INE5421"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "Expressão Regular"))
        self.pushButton.setText(_translate("MainWindow", "Carregar ER"))
        # self.pushButton.clicked.connect(self.carrega_regex())
        self.pushButton_2.setText(_translate("MainWindow", "Gravar ER"))
        self.pushButton_3.setText(_translate("MainWindow", "Adicionar Transição"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.pushButton_4.setText(_translate("MainWindow", "Completar"))
        self.pushButton_5.setText(_translate("MainWindow", "Complemento"))
        self.pushButton_6.setText(_translate("MainWindow", "Minimizar"))
        self.pushButton_7.setText(_translate("MainWindow", "União"))
        self.pushButton_8.setText(_translate("MainWindow", "Interseção"))

    def salva_regex(self):
        nome = self.lineEdit_2.text()
        if nome != "":
            self.RegEx.set_expression(self.lineEdit.text())
            self.RegEx.save_expression(nome)

    def carrega_regex(self):
        nome = self.lineEdit_2.text()
        if nome != "":
            self.RegEx.load_expression(nome)
            self.lineEdit.setText(self.RegEx.expression)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

