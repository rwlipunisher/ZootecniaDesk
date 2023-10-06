from PyQt6.QtWidgets import ( QSplashScreen, QMainWindow, 
                             QLabel,
                             QPushButton, QWidget,  
                             QMenuBar,
                             QPushButton, QCheckBox, QCommandLinkButton, 
                             QStatusBar, QTextEdit, QWidget)
from PyQt6.QtCore import (Qt, QCoreApplication, QMetaObject, QRect)
from PyQt6.QtGui import QPixmap, QFont, QIcon
from PyQt6 import QtCore
import os
import time
from Controller import *

class SplashScreen(QSplashScreen):
    def __init__(self):
        super().__init__(QPixmap(os.path.join(os.path.dirname(os.path.abspath(__file__)), "splash_image.png")))

    def show_message(self, message):
        self.showMessage(message, QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignCenter, QtCore.Qt.GlobalColor.black)
        time.sleep(1)

class ViewLogin(QMainWindow):
    pass
class ViewErrorSystemRestart(QMainWindow):
     def __init__(self):
        super().__init__()
        self.setWindowTitle("Erro!")
        # Create a QLabel widget to display "Hello, World!"
        hello_label = QLabel("Ocorreu um erro, reinicie o computador e tente novamente", self)
        hello_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        hello_label.setStyleSheet("font-size: 24px;")
        # Set the central widget to the QLabel
        self.setCentralWidget(hello_label)


class WindowInitialUserActivation(QMainWindow):
    def setupUi(self, MainWindow: QMainWindow) -> None:
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(458, 519)
        MainWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.setWindowIcon(QIcon(u"Resources/images/SystemImages/icon.png"))
        self.TokenAcitaveteWindow = QWidget(MainWindow)
        self.TokenAcitaveteWindow.setObjectName(u"TokenAcitaveteWindow")
        self.label = QLabel(self.TokenAcitaveteWindow)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 40, 351, 411))
        self.label.setStyleSheet(u"border-image: url(Resources/images/SystemImages/initsettingsBG.jpeg);\n"
"border-radius: 20px;")
        self.label_2 = QLabel(self.TokenAcitaveteWindow)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(100, 70, 271, 371))
        self.label_2.setStyleSheet(u"border-radius: 20px; \n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 49), stop:1 rgba(255, 255, 255, 255));\n"
"background-color: rgba(0, 0, 0, 100);")
        self.label_3 = QLabel(self.TokenAcitaveteWindow)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 90, 181, 31))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color:rgba(255, 255, 255, 100);\n"
"color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.label_4 = QLabel(self.TokenAcitaveteWindow)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(110, 130, 251, 31))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setKerning(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color:rgba(255, 255, 255, 100);\n"
"color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.textEdit = QTextEdit(self.TokenAcitaveteWindow)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(110, 190, 241, 31))
        self.textEdit_2 = QTextEdit(self.TokenAcitaveteWindow)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(110, 250, 241, 31))
        self.commandLinkButton = QCommandLinkButton(self.TokenAcitaveteWindow)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setGeometry(QRect(130, 310, 185, 41))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(True)
        self.commandLinkButton.setFont(font2)
        self.commandLinkButton.setStyleSheet(u"color:rgb(255, 255, 255);")
        MainWindow.setCentralWidget(self.TokenAcitaveteWindow)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 458, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)
        fdliahfoçaheafhbaew nada ve r lakdj eroier pa 
        self.commandLinkButton.clicked.connect(FirstRunSoftware.checkTokenCPF(self.textEdit, self.textEdit_2, ))

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ativar Software", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bem Vindo!", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Digite o Token e CPF Para Continuar", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite Aqui o Token", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite aqui seu CPF", None))
        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Continuar Configura\u00e7\u00e3o", None))
    # retranslateUi


class WindowInitialConfig(QMainWindow):
    def setupUi(self, MainWindow: QMainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(530, 569)
        MainWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 30, 431, 461))
        self.widget.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 56), stop:1 rgba(255, 255, 255, 255));")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 0, 261, 41))
        font = QFont()
        font.setPointSize(26)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 230, 201, 16))
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 80, 281, 31))
        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(300, 80, 104, 31))
        self.textEdit_3 = QTextEdit(self.widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(10, 120, 151, 31))
        self.textEdit_4 = QTextEdit(self.widget)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(180, 120, 121, 31))
        self.checkBox = QCheckBox(self.widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(310, 130, 76, 20))
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(90, 50, 241, 16))
        self.textEdit_9 = QTextEdit(self.widget)
        self.textEdit_9.setObjectName(u"textEdit_9")
        self.textEdit_9.setGeometry(QRect(10, 260, 241, 31))
        self.textEdit_10 = QTextEdit(self.widget)
        self.textEdit_10.setObjectName(u"textEdit_10")
        self.textEdit_10.setGeometry(QRect(10, 300, 241, 31))
        self.textEdit_11 = QTextEdit(self.widget)
        self.textEdit_11.setObjectName(u"textEdit_11")
        self.textEdit_11.setGeometry(QRect(260, 260, 161, 31))
        self.textEdit_12 = QTextEdit(self.widget)
        self.textEdit_12.setObjectName(u"textEdit_12")
        self.textEdit_12.setGeometry(QRect(260, 300, 161, 31))
        self.checkBox_3 = QCheckBox(self.widget)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(10, 340, 81, 20))
        self.checkBox_4 = QCheckBox(self.widget)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(100, 340, 111, 20))
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 180, 331, 41))
        self.label_8.setFont(font)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 380, 241, 61))
        font1 = QFont()
        font1.setPointSize(20)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 71));")
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 10, 451, 521))
        self.label_7.setStyleSheet(u"border-image: url(Resources/images/SystemImages/initsettingsBG.jpeg);\n"
"border-radius: 20px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.label_7.raise_()
        self.widget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow: QMainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Dados Pessoais", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Digite os Dados do Empreendimento", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nascimento", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Usuario do Sistema", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha de Acesso", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"Sem Senha", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Digite seus dados e Crie sua Conta de Acesso.", None))
        self.textEdit_9.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome da Empresa", None))
        self.textEdit_10.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF ou CNPJ", None))
        self.textEdit_11.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Inicio da Empresa", None))
        self.textEdit_12.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de Inicio na Associa\u00e7\u00e3o", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"Sou Criador", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"Sou Propriet\u00e1rio", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Dados Empresariais", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Criar Acesso", None))
        self.label_7.setText("")
    # retranslateUi

