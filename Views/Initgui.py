from PyQt6.QtCore import Qt, QRegularExpression, QRect
from PyQt6.QtGui import QPixmap, QRegularExpressionValidator, QGuiApplication
from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import  QSplashScreen, QMainWindow, QWidget, QApplication
from .GeralInterface import MainWindowApp
import os
import sys
import time
import sqlite3

from Controller import ToolsControllsInitialSettings

class SplashScreen(QSplashScreen):
    def __init__(self, mainDir):
        super().__init__(QPixmap(mainDir+"\Resources\images\SystemImages\splash_image.png"))

    def show_message(self, message):
        self.showMessage(message, QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignCenter, QtCore.Qt.GlobalColor.black)
        time.sleep(2)

class InitUserInterfaces(object):

    def __init__(self, MainWindow:  QMainWindow, mainDir: str ) -> None:
        self.MainWindow = MainWindow
        self.mainDir = mainDir
        self.MainWindow.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.MainWindow.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.MainWindow.setWindowTitle('Centered MainWindow')
        self.MainWindow.setGeometry(100, 100, 800, 600)  # Set an initial size, which can be adjusted later
        p_screen = QGuiApplication.primaryScreen()
        screen = p_screen.availableGeometry()
        x = (screen.width() - self.MainWindow.width()) // 2
        y = (screen.height() - self.MainWindow.height()) // 2
        self.MainWindow.move(x, y)
        self.dictInit = {}
        self.MainWindow.show()

    def initialAccessUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(689, 733)
        centralwidget = QtWidgets.QWidget(parent=self.MainWindow)
        centralwidget.setObjectName("centralwidget")
        label_3 = QtWidgets.QLabel(parent=centralwidget)
        label_3.setGeometry(QtCore.QRect(40, 50, 611, 601))
        label_3.setStyleSheet("border-image: url("+self.mainDir+"\Resources\images\SystemImages\initsettingsBG.png);\n"
        "border-radius:20px;")
        label_3.setText("")
        label_3.setObjectName("label_3")
        label_4 = QtWidgets.QLabel(parent=centralwidget)
        label_4.setGeometry(QtCore.QRect(100, 70, 491, 551))
        label_4.setStyleSheet("border-radius: 20px;\n"
        "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 89));")
        label_4.setText("")
        label_4.setObjectName("label_4")
        label_5 = QtWidgets.QLabel(parent=centralwidget)
        label_5.setGeometry(QtCore.QRect(220, 90, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        label_5.setFont(font)
        label_5.setStyleSheet("color: rgb(255, 255, 255);")
        label_5.setObjectName("label_5")
        label_9 = QtWidgets.QLabel(parent=centralwidget)
        label_9.setGeometry(QtCore.QRect(180, 310, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        label_9.setFont(font)
        label_9.setStyleSheet("color: rgb(255, 255, 255);")
        label_9.setObjectName("label_9")
        lineEdit = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit.setGeometry(QtCore.QRect(120, 190, 291, 32))
        lineEdit.setObjectName("lineEdit")
        label_7 = QtWidgets.QLabel(parent=centralwidget)
        label_7.setGeometry(QtCore.QRect(170, 130, 391, 31))
        label_7.setStyleSheet("color: rgb(255, 255, 255);")
        label_7.setObjectName("label_7")
        lineEdit_2 = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit_2.setGeometry(QtCore.QRect(420, 190, 151, 32))
        lineEdit_2.setObjectName("lineEdit_2")
        lineEdit_3 = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit_3.setGeometry(QtCore.QRect(120, 230, 191, 32))
        lineEdit_3.setText("")
        lineEdit_3.setObjectName("lineEdit_3")
        lineEdit_4 = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit_4.setGeometry(QtCore.QRect(320, 230, 151, 32))
        lineEdit_4.setText("")
        lineEdit_4.setObjectName("lineEdit_4")
        checkBox_4 = QtWidgets.QCheckBox(parent=centralwidget)
        checkBox_4.setGeometry(QtCore.QRect(480, 240, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        checkBox_4.setFont(font)
        checkBox_4.setStyleSheet("color: rgb(255, 255, 255);")
        checkBox_4.setObjectName("checkBox_4")
        lineEdit_5 = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit_5.setGeometry(QtCore.QRect(120, 380, 361, 32))
        lineEdit_5.setText("")
        lineEdit_5.setObjectName("lineEdit_5")
        lineEdit_6 = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit_6.setGeometry(QtCore.QRect(120, 420, 261, 32))
        lineEdit_6.setText("")
        lineEdit_6.setObjectName("lineEdit_6")
        checkBox_5 = QtWidgets.QCheckBox(parent=centralwidget)
        checkBox_5.setGeometry(QtCore.QRect(120, 460, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        checkBox_5.setFont(font)
        checkBox_5.setStyleSheet("color: rgb(255, 255, 255);")
        checkBox_5.setObjectName("checkBox_5")
        font = QtGui.QFont()
        font.setPointSize(10)
        pushButton = QtWidgets.QPushButton(parent=centralwidget)
        pushButton.setGeometry(QtCore.QRect(210, 500, 261, 34))
        pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(119, 255, 142, 122));\n"
        "color: rgb(255, 255, 255);")
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(parent=centralwidget)
        pushButton_2.setGeometry(QtCore.QRect(260, 540, 161, 34))
        pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(230, 181, 5, 115));\n"
        "color: rgb(255, 255, 255);")
        pushButton_2.setObjectName("pushButton_2")
        self.MainWindow.setCentralWidget(centralwidget)
        label_5.setText("Dados Pessoais")
        label_9.setText("Dados Empresariais")
        lineEdit.setPlaceholderText("Nome Completo")
        label_7.setText("Digite seus dados e Crie sua Conta de Acesso.")
        lineEdit_2.setPlaceholderText("Nascimento")
        lineEdit_3.setPlaceholderText("Usuario")
        lineEdit_4.setPlaceholderText("Senha")
        checkBox_4.setText("Sem Senha")
        lineEdit_5.setPlaceholderText("Nome da Empresa")
        lineEdit_6.setPlaceholderText("CPF ou CNPJ")
        checkBox_5.setText("Criador")
        pushButton.setText("Analisar Dados")
        pushButton_2.setText("Cancelar")
        pushButton_2.clicked.connect(QApplication.quit)
        pushButton.clicked.connect(self.checkDataToCreateUser)

    def tokenCpfInitUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(500, 500)
        centralwidget = QWidget(self.MainWindow)
        centralwidget.setObjectName("centralwidget")
        label = QtWidgets.QLabel(parent=centralwidget)
        label.setGeometry(QtCore.QRect(60, 40, 351, 411))
        label.setStyleSheet("border-image: url(Resources/images/SystemImages/initsettingsBG.png);\n"
        "border-radius: 20px;")
        label.setText("")
        label.setObjectName("label")
        label_2 = QtWidgets.QLabel(parent=centralwidget)
        label_2.setGeometry(QtCore.QRect(100, 70, 271, 371))
        label_2.setStyleSheet("border-radius: 20px; \n"
        "color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 49), stop:1 rgba(255, 255, 255, 255));\n"
        "background-color: rgba(0, 0, 0, 100);")
        label_2.setText("")
        label_2.setObjectName("label_2")
        label_3 = QtWidgets.QLabel(parent=centralwidget)
        label_3.setGeometry(QtCore.QRect(140, 90, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setKerning(True)
        label_3.setFont(font)
        label_3.setStyleSheet("color:rgba(255, 255, 255, 100);\n"
        "color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "")
        label_3.setObjectName("label_3")
        label_4 = QtWidgets.QLabel(parent=centralwidget)
        label_4.setGeometry(QtCore.QRect(110, 130, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setKerning(True)
        label_4.setFont(font)
        label_4.setStyleSheet("color:rgba(255, 255, 255, 100);\n"
        "color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 0, 0, 255), stop:0.479904 rgba(255, 0, 0, 255), stop:0.522685 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
        "")
        label_4.setObjectName("label_4")
        lineEdit = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit.setGeometry(QtCore.QRect(120, 210, 231, 32))
        lineEdit.setObjectName("lineEdit")
        lineEdit_2 = QtWidgets.QLineEdit(parent=centralwidget)
        lineEdit_2.setGeometry(QtCore.QRect(120, 270, 231, 32))
        lineEdit_2.setObjectName("lineEdit_2")
        pushButton = QtWidgets.QPushButton(parent=centralwidget)
        pushButton.setGeometry(QtCore.QRect(130, 330, 201, 34))
        pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 112));\n"
        "color: rgb(255, 255, 255);")
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(parent=centralwidget)
        pushButton_2.setGeometry(QtCore.QRect(130, 390, 201, 34))
        pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(230, 181, 5, 115));\n"
        "color: rgb(255, 255, 255);")
        self.MainWindow.setWindowTitle("Ativar Software")
        label_3.setText("Bem Vindo!")
        label_4.setText("Digite o Token e CPF Para Continuar")
        lineEdit.setPlaceholderText("Digite seu CPF Aqui")
        lineEdit_2.setPlaceholderText("Digite o Token Aqui")
        pushButton.setText("Continuar")
        pushButton_2.setText("Cancelar")
        pushButton_2.setObjectName("pushButton_2")
        self.MainWindow.setCentralWidget(centralwidget)
        pushButton.clicked.connect(self.changeToinitialAccessUi)
        pushButton_2.clicked.connect(QApplication.quit)

    def loginUi(self):
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(500, 500)
        centralwidget = QWidget(self.MainWindow)
        centralwidget.setObjectName("centralwidget")
        label = QtWidgets.QLabel(centralwidget)
        label.setGeometry(QtCore.QRect(140, 80, 291, 411))
        label.setStyleSheet("border-image: url(:/here/initsettingsBG.png);\n"
        "border-radius: 20px;")
        label.setText("")
        label.setObjectName("label")
        label_2 = QtWidgets.QLabel(centralwidget)
        label_2.setGeometry(QtCore.QRect(170, 120, 241, 341))
        label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 89));\n"
        "border-radius: 20px;")
        label_2.setText("")
        label_2.setObjectName("label_2")
        label_3 = QtWidgets.QLabel(centralwidget)
        label_3.setGeometry(QtCore.QRect(230, 140, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        label_3.setFont(font)
        label_3.setStyleSheet("color: rgb(255, 255, 255);")
        label_3.setObjectName("label_3")
        lineEdit = QtWidgets.QLineEdit(centralwidget)
        lineEdit.setGeometry(QtCore.QRect(190, 220, 191, 32))
        lineEdit.setObjectName("lineEdit")
        lineEdit_2 = QtWidgets.QLineEdit(centralwidget)
        lineEdit_2.setGeometry(QtCore.QRect(190, 270, 191, 32))
        lineEdit_2.setObjectName("lineEdit_2")
        pushButton = QtWidgets.QPushButton(centralwidget)
        pushButton.setGeometry(QtCore.QRect(230, 320, 105, 34))
        font = QtGui.QFont()
        font.setBold(False)
        pushButton.setFont(font)
        pushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(119, 255, 142, 122));\n"
        "color: rgb(255, 255, 255);")
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(centralwidget)
        pushButton_2.setGeometry(QtCore.QRect(230, 360, 105, 34))
        pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(230, 181, 5, 115));\n"
        "color: rgb(255, 255, 255);")
        pushButton_2.setObjectName("pushButton_2")
        label_3.setText("Login")
        lineEdit.setPlaceholderText("usuario")
        lineEdit_2.setPlaceholderText("senha")
        pushButton.setText("Entrar")
        pushButton_2.setText("Cancelar")
        self.MainWindow.setCentralWidget(centralwidget)
        pushButton.clicked.connect(self.login)
        pushButton_2.clicked.connect(QApplication.quit)
    
    def checkDataToCreateUser(self):
        #get all data in to a listea
        dictAux = {}
        dictAux["name"] = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit").text()
        dictAux["nascimento"] = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_2").text()
        dictAux["nomeEmpresa"] = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_5").text()

        for key, value in dictAux.items():
            if not value: 
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Mensagem de Erro")
                msg_box.setText(f"O campo {key} é obrigatorio!")
                msg_box.exec()
                return
        
        dictAux["cpfOrCnpj"] = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_6").text()
        if not ToolsControllsInitialSettings.checkCnpj(dictAux["cpfOrCnpj"]):
            if not ToolsControllsInitialSettings.checkCpf(dictAux["cpfOrCnpj"]):
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Mensagem de Erro")
                msg_box.setText("Confira o CPF ou CNPJ digitado e tente novamente!")
                msg_box.exec()
                return

        dictAux["senha"] = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_4").text()
        dictAux["sem_senha"] = self.MainWindow.findChild(QtWidgets.QCheckBox, "checkBox_4").isChecked()
        if not dictAux["sem_senha"]:
            if len(dictAux["senha"]) > 6 or len(dictAux["senha"]) < 3:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Mensagem de Erro")
                msg_box.setText("Senha incorreta, deve conter de 3 a 6 digitos apenas")
                msg_box.exec()
                return
        else:
            dictAux["senha"] = "0000"

        dictAux["user_name"] = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_3").text()
        if len(dictAux["user_name"]) < 4:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Mensagem de Erro")
            msg_box.setText("O nome de usuario deve conter mais do que 3 digitos")
            msg_box.exec()
            return



        self.dictInit.update(dictAux)
        self.dictInit["criador"] = self.MainWindow.findChild(QtWidgets.QCheckBox, "checkBox_5").isChecked()
        self.firstDataBaseUserWrite()

    def login(self):
        user = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit").text()
        senha = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_2").text()
        db_path = os.path.join(self.mainDir+ "\Resources\DataBase\main.db")
        connection = sqlite3.connect(str(db_path))
        cursor = connection.cursor()
        result = cursor.execute('SELECT user_name, senha FROM user_access_data WHERE id=1').fetchone()
        connection.close()
        duser, dsenha = result
        if duser == user:
            if dsenha == senha:
                self.MainWindow.centralWidget().deleteLater()
                main = MainWindowApp()
                main.setupUi(self.MainWindow)
            else: 
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Aviso de Erro!")
                msg_box.setText("Senha incorreta Tente Novamente")
                msg_box.exec()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Aviso de Erro!")
            msg_box.setText("Usuario nao existe")
            msg_box.exec()
        

    def firstDataBaseUserWrite(self):    
        try:
            db_path = os.path.join(self.mainDir+ "\Resources\DataBase\main.db")
            connection = sqlite3.connect(str(db_path))
            cursor = connection.cursor()
            insert_sql = f'''UPDATE user_access_data
                            SET cpf = '{self.dictInit["cpf"]}',
                                token = '{self.dictInit["token"]}',
                                name = '{self.dictInit["name"]}',
                                nascimento ='{self.dictInit["nascimento"]}',
                                user_name = '{self.dictInit["user_name"]}',
                                nomeEmpresa = '{self.dictInit["nomeEmpresa"]}',
                                cpfOrCnpj = '{self.dictInit["cpfOrCnpj"]}',
                                senha = '{self.dictInit["senha"]}',
                                sem_senha = '{self.dictInit["sem_senha"]}',
                                criador = '{self.dictInit["criador"]}'
                            WHERE id = 1'''
            
            #insert_sql = "INSERT INTO user_access_data (cpf, token, name, nascimento, user_name, nomeEmpresa, cpfOrCnpj, senha, sem_senha, criador) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(insert_sql)
            connection.commit()
            connection.close()
        except sqlite3.Error as e:
            print(e, "Esse Erro")
        
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Mensagem de Erro")
        msg_box.setText("Seus dados de Acesso, copie e cole se precisar: user, senha")
        msg_box.exec()
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    def changeToinitialAccessUi(self):
        cpf = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit")
        token = self.MainWindow.findChild(QtWidgets.QLineEdit, "lineEdit_2")
        if ToolsControllsInitialSettings.checkCpf(cpf.text()):
            if ToolsControllsInitialSettings.checkToken(token.text()):
                self.MainWindow.findChild(QtWidgets.QLineEdit, "LineEdit")
                self.dictInit["cpf"] = cpf.text()
                self.dictInit["token"] = token.text()
                self.MainWindow.centralWidget().deleteLater()
                self.initialAccessUi() 
            else:
                msg_box = QtWidgets.QMessageBox()
                msg_box.setWindowTitle("Aviso de Erro!")
                msg_box.setText("O Token não é Valido")
                msg_box.exec()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Aviso de Erro!")
            msg_box.setText("O CPF esta incorreto")
            msg_box.exec()



