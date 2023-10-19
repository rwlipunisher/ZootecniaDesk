from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtCore import Qt
import sqlite3
import shutil
import os
from Controller import *

class MainWindowApp():
    
    def setupUi(self, MainWindow: QMainWindow, mainDir: str, personalDir: str):
        self.mainDir = mainDir
        self.personalDir = personalDir
        self.MainWindow = MainWindow
        print(self.personalDir)
        self.mainDatabasePath = os.path.join(mainDir+ "\Resources\DataBase\main.db")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1032, 688)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(25, 25, 25);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_header = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_header.setMaximumSize(QtCore.QSize(16777215, 50))
        self.main_header.setStyleSheet("QFrame{\n"
"    border-bottom: 1px solid #000;\n"
"    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.main_header.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.main_header.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_header.setObjectName("main_header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.main_header)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tittle_bar_container = QtWidgets.QFrame(parent=self.main_header)
        self.tittle_bar_container.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tittle_bar_container.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tittle_bar_container.setObjectName("tittle_bar_container")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tittle_bar_container)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_menu_toggle = QtWidgets.QFrame(parent=self.tittle_bar_container)
        self.left_menu_toggle.setMinimumSize(QtCore.QSize(50, 0))
        self.left_menu_toggle.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_menu_toggle.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 5px 10px;\n"
"    border: none;\n"
"    border-radius: 5px;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.left_menu_toggle.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_menu_toggle.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_menu_toggle.setObjectName("left_menu_toggle")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.left_menu_toggle)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_5.addWidget(self.left_menu_toggle)
        self.tittle_bar = QtWidgets.QFrame(parent=self.tittle_bar_container)
        self.tittle_bar.setStyleSheet("QLabel{\n"
"    color: #fff;\n"
"}")
        self.tittle_bar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.tittle_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.tittle_bar.setObjectName("tittle_bar")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.tittle_bar)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_6 = QtWidgets.QLabel(parent=self.tittle_bar)
        font = QtGui.QFont()
        font.setFamily("Open Sans Semibold")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.horizontalLayout_5.addWidget(self.tittle_bar)
        self.horizontalLayout_2.addWidget(self.tittle_bar_container)
        self.top_right_btns = QtWidgets.QFrame(parent=self.main_header)
        self.top_right_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.top_right_btns.setStyleSheet("QPushButton{\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.top_right_btns.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_right_btns.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_right_btns.setObjectName("top_right_btns")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.top_right_btns)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.restoreButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.restoreButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.restoreButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/cil-window-maximize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.restoreButton.setIcon(icon)
        self.restoreButton.setIconSize(QtCore.QSize(24, 24))
        self.restoreButton.setObjectName("restoreButton")
        self.horizontalLayout_3.addWidget(self.restoreButton)
        self.minimizeButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.minimizeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.minimizeButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/cil-minus.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.minimizeButton.setIcon(icon1)
        self.minimizeButton.setIconSize(QtCore.QSize(24, 24))
        self.minimizeButton.setObjectName("minimizeButton")
        self.horizontalLayout_3.addWidget(self.minimizeButton)
        self.closeButton = QtWidgets.QPushButton(parent=self.top_right_btns)
        self.closeButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/cil-x.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setIconSize(QtCore.QSize(24, 24))
        self.closeButton.setObjectName("closeButton")
        self.horizontalLayout_3.addWidget(self.closeButton)
        self.horizontalLayout_2.addWidget(self.top_right_btns)
        self.verticalLayout.addWidget(self.main_header)
        self.main_body = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_body.setObjectName("main_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.main_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_side_menu = QtWidgets.QFrame(parent=self.main_body)
        self.left_side_menu.setMaximumSize(QtCore.QSize(50, 16777215))
        self.left_side_menu.setStyleSheet("QFrame{\n"
"    background-color: #000;\n"
"}\n"
"QPushButton{\n"
"    padding: 20px 10px;\n"
"    border: none;\n"
"    border-left: 2px solid transparent;\n"
"    border-bottom: 2px solid transparent;\n"
"    border-radius: 5px;\n"
"    background-color: #000;\n"
"    color: #fff;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(0, 92, 157);\n"
"    border-bottom: 2px solid rgb(255, 165, 24);\n"
"}")
        self.left_side_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.left_side_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_side_menu.setObjectName("left_side_menu")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_side_menu)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.left_menu_top_buttons = QtWidgets.QFrame(parent=self.left_side_menu)
        self.left_menu_top_buttons.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.left_menu_top_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.left_menu_top_buttons.setObjectName("left_menu_top_buttons")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.left_menu_top_buttons)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.buscasPushButton = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.buscasPushButton.setStyleSheet("background-image: url(:/bgincons/home.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-color: rgb(122, 123, 145);\n"
"background-position: center;\n"
"color:rgb(255,255,255);")
        self.buscasPushButton.setText("")
        self.buscasPushButton.setObjectName("buscasPushButton")
        self.verticalLayout_6.addWidget(self.buscasPushButton)
        self.configuracoespushButton = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.configuracoespushButton.setStyleSheet("background-image: url(:/bgincons/home.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center;\n"
"color:rgb(255,255,255);\n"
"background-color: rgb(122, 123, 145);\n"
"")
        self.configuracoespushButton.setText("")
        self.configuracoespushButton.setObjectName("configuracoespushButton")
        self.verticalLayout_6.addWidget(self.configuracoespushButton)
        self.cadastrospushButton = QtWidgets.QPushButton(parent=self.left_menu_top_buttons)
        self.cadastrospushButton.setStyleSheet("background-image: url(:/bgincons/home.png);\n"
"background-repeat: none;\n"
"padding-left: 50px;\n"
"background-position: center;\n"
"color:rgb(255,255,255);\n"
"background-color: rgb(122, 123, 145);\n"
"")
        self.cadastrospushButton.setText("")
        self.cadastrospushButton.setObjectName("cadastrospushButton")
        self.verticalLayout_6.addWidget(self.cadastrospushButton)
        self.verticalLayout_3.addWidget(self.left_menu_top_buttons)
        self.horizontalLayout.addWidget(self.left_side_menu)
        self.center_main_items = QtWidgets.QFrame(parent=self.main_body)
        self.center_main_items.setStyleSheet("")
        self.center_main_items.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.center_main_items.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.center_main_items.setObjectName("center_main_items")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.center_main_items)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.center_main_items)
        self.stackedWidget.setMidLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_11 = QtWidgets.QFrame(parent=self.page)
        self.frame_11.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_11)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_14 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_14.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_14.setObjectName("frame_14")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_14)
        self.formLayout_3.setObjectName("formLayout_3")
        self.frame_17 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_17.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_17.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_17.setObjectName("frame_17")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_17)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_13 = QtWidgets.QLabel(parent=self.frame_17)
        self.label_13.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.label_13.setObjectName("label_13")
        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)
        self.arquivo = QtWidgets.QLineEdit(parent=self.frame_17)
        self.arquivo.setStyleSheet("color: rgb(255,255,255);")
        self.arquivo.setText("")
        self.arquivo.setObjectName("arquivo")
        self.gridLayout_2.addWidget(self.arquivo, 1, 0, 1, 1)
        self.importarAnimaispushButton = QtWidgets.QPushButton(parent=self.frame_17)
        self.importarAnimaispushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.importarAnimaispushButton.setObjectName("importarAnimaispushButton")
        self.gridLayout_2.addWidget(self.importarAnimaispushButton, 3, 0, 1, 2)
        self.tipoImportacaoAnimaiscomboBox = QtWidgets.QComboBox(parent=self.frame_17)
        self.tipoImportacaoAnimaiscomboBox.setObjectName("tipoImportacaoAnimaiscomboBox")
        self.tipoImportacaoAnimaiscomboBox.addItem("")
        self.tipoImportacaoAnimaiscomboBox.addItem("")
        self.gridLayout_2.addWidget(self.tipoImportacaoAnimaiscomboBox, 2, 0, 1, 2)
        self.escolherArquivoImportacaoAnaimaispushButton = QtWidgets.QPushButton(parent=self.frame_17)
        self.escolherArquivoImportacaoAnaimaispushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.escolherArquivoImportacaoAnaimaispushButton.setObjectName("escolherArquivoImportacaoAnaimaispushButton")
        self.gridLayout_2.addWidget(self.escolherArquivoImportacaoAnaimaispushButton, 1, 1, 1, 1)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.frame_17)
        self.frame_18 = QtWidgets.QFrame(parent=self.frame_14)
        self.frame_18.setStyleSheet("color: rgb(255, 255, 255);\n"
"\n"
"")
        self.frame_18.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_18.setObjectName("frame_18")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.frame_18)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.esclhoerArquivoImportacaoTerceiropushButton = QtWidgets.QPushButton(parent=self.frame_18)
        self.esclhoerArquivoImportacaoTerceiropushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.esclhoerArquivoImportacaoTerceiropushButton.setObjectName("esclhoerArquivoImportacaoTerceiropushButton")
        self.gridLayout_8.addWidget(self.esclhoerArquivoImportacaoTerceiropushButton, 1, 1, 1, 1)
        self.tipoImportacaoTerceirocomboBox = QtWidgets.QComboBox(parent=self.frame_18)
        self.tipoImportacaoTerceirocomboBox.setObjectName("tipoImportacaoTerceirocomboBox")
        self.tipoImportacaoTerceirocomboBox.addItem("")
        self.tipoImportacaoTerceirocomboBox.addItem("")
        self.gridLayout_8.addWidget(self.tipoImportacaoTerceirocomboBox, 2, 0, 1, 2)
        self.lineEdit_11 = QtWidgets.QLineEdit(parent=self.frame_18)
        self.lineEdit_11.setStyleSheet("color: rgb(255,255,255);")
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout_8.addWidget(self.lineEdit_11, 1, 0, 1, 1)
        self.importarTerceirospushButton = QtWidgets.QPushButton(parent=self.frame_18)
        self.importarTerceirospushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.importarTerceirospushButton.setObjectName("importarTerceirospushButton")
        self.gridLayout_8.addWidget(self.importarTerceirospushButton, 3, 0, 1, 2)
        self.label_14 = QtWidgets.QLabel(parent=self.frame_18)
        self.label_14.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.label_14.setObjectName("label_14")
        self.gridLayout_8.addWidget(self.label_14, 0, 0, 1, 2)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.frame_18)
        self.label_11 = QtWidgets.QLabel(parent=self.frame_14)
        self.label_11.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.ItemRole.SpanningRole, self.label_11)
        self.gridLayout_10.addWidget(self.frame_14, 0, 1, 1, 2)
        self.frame_15 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_15.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_15.setObjectName("frame_15")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame_15)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.backupSeguranapushButton = QtWidgets.QPushButton(parent=self.frame_15)
        self.backupSeguranapushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.backupSeguranapushButton.setObjectName("backupSeguranapushButton")
        self.gridLayout_11.addWidget(self.backupSeguranapushButton, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.frame_15)
        self.label_12.setMinimumSize(QtCore.QSize(0, 20))
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 2))
        self.label_12.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.label_12.setObjectName("label_12")
        self.gridLayout_11.addWidget(self.label_12, 2, 0, 1, 1)
        self.backupAssocialpushButton = QtWidgets.QPushButton(parent=self.frame_15)
        self.backupAssocialpushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.backupAssocialpushButton.setObjectName("backupAssocialpushButton")
        self.gridLayout_11.addWidget(self.backupAssocialpushButton, 6, 0, 1, 1)
        self.selectMainDirpushButton = QtWidgets.QPushButton(parent=self.frame_15)
        self.selectMainDirpushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.selectMainDirpushButton.setObjectName("selectMainDirpushButton")
        self.gridLayout_11.addWidget(self.selectMainDirpushButton, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame_15, 1, 2, 1, 1)
        self.frame_13 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_13.setObjectName("frame_13")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_13)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.nomePerfilAcessolineEdit = QtWidgets.QLineEdit(parent=self.frame_13)
        self.nomePerfilAcessolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.nomePerfilAcessolineEdit.setText("")
        self.nomePerfilAcessolineEdit.setObjectName("nomePerfilAcessolineEdit")
        self.gridLayout_9.addWidget(self.nomePerfilAcessolineEdit, 1, 0, 1, 1)
        self.cpfPerfilAcessolineEdit = QtWidgets.QLineEdit(parent=self.frame_13)
        self.cpfPerfilAcessolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.cpfPerfilAcessolineEdit.setText("")
        self.cpfPerfilAcessolineEdit.setObjectName("cpfPerfilAcessolineEdit")
        self.gridLayout_9.addWidget(self.cpfPerfilAcessolineEdit, 1, 1, 1, 1)
        self.nascimentoPerfilAcessolineEdit = QtWidgets.QLineEdit(parent=self.frame_13)
        self.nascimentoPerfilAcessolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.nascimentoPerfilAcessolineEdit.setObjectName("nascimentoPerfilAcessolineEdit")
        self.gridLayout_9.addWidget(self.nascimentoPerfilAcessolineEdit, 3, 0, 1, 1)
        self.senhaPerfilAcessocheckBox = QtWidgets.QCheckBox(parent=self.frame_13)
        self.senhaPerfilAcessocheckBox.setStyleSheet("color:rgb(255,255,255);")
        self.senhaPerfilAcessocheckBox.setObjectName("senhaPerfilAcessocheckBox")
        self.gridLayout_9.addWidget(self.senhaPerfilAcessocheckBox, 3, 2, 1, 1)
        self.cpfOuCnpjPerfilAcessolineEdit = QtWidgets.QLineEdit(parent=self.frame_13)
        self.cpfOuCnpjPerfilAcessolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.cpfOuCnpjPerfilAcessolineEdit.setText("")
        self.cpfOuCnpjPerfilAcessolineEdit.setObjectName("cpfOuCnpjPerfilAcessolineEdit")
        self.gridLayout_9.addWidget(self.cpfOuCnpjPerfilAcessolineEdit, 2, 1, 1, 1)
        self.cpfPerfilAcessolineEdit_2 = QtWidgets.QLineEdit(parent=self.frame_13)
        self.cpfPerfilAcessolineEdit_2.setStyleSheet("color: rgb(255,255,255);")
        self.cpfPerfilAcessolineEdit_2.setObjectName("cpfPerfilAcessolineEdit_2")
        self.gridLayout_9.addWidget(self.cpfPerfilAcessolineEdit_2, 2, 0, 1, 1)
        self.alterarAcessosPerfilAcessospushButton = QtWidgets.QPushButton(parent=self.frame_13)
        self.alterarAcessosPerfilAcessospushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.alterarAcessosPerfilAcessospushButton.setObjectName("alterarAcessosPerfilAcessospushButton")
        self.gridLayout_9.addWidget(self.alterarAcessosPerfilAcessospushButton, 4, 1, 1, 1)
        self.senhaPerfilAcessolineEdit = QtWidgets.QLineEdit(parent=self.frame_13)
        self.senhaPerfilAcessolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.senhaPerfilAcessolineEdit.setObjectName("senhaPerfilAcessolineEdit")
        self.gridLayout_9.addWidget(self.senhaPerfilAcessolineEdit, 2, 2, 1, 1)
        self.nomeUsuarioPerfilAcessolineEdit = QtWidgets.QLineEdit(parent=self.frame_13)
        self.nomeUsuarioPerfilAcessolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.nomeUsuarioPerfilAcessolineEdit.setObjectName("nomeUsuarioPerfilAcessolineEdit")
        self.gridLayout_9.addWidget(self.nomeUsuarioPerfilAcessolineEdit, 1, 2, 1, 1)
        self.criadorPerfilAcessocheckBox = QtWidgets.QCheckBox(parent=self.frame_13)
        self.criadorPerfilAcessocheckBox.setStyleSheet("color:rgb(255,255,255);")
        self.criadorPerfilAcessocheckBox.setObjectName("criadorPerfilAcessocheckBox")
        self.gridLayout_9.addWidget(self.criadorPerfilAcessocheckBox, 3, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.frame_13)
        self.label_10.setMinimumSize(QtCore.QSize(0, 20))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_10.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.label_10.setObjectName("label_10")
        self.gridLayout_9.addWidget(self.label_10, 0, 0, 1, 3)
        self.gridLayout_10.addWidget(self.frame_13, 1, 0, 1, 2)
        self.frame_12 = QtWidgets.QFrame(parent=self.frame_11)
        self.frame_12.setStyleSheet("border-radius: 20px;")
        self.frame_12.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_12.setObjectName("frame_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_12)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_12)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setStyleSheet("color:rgb(255,255,255);\n"
"")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.frame_16 = QtWidgets.QFrame(parent=self.frame_12)
        self.frame_16.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_16.setObjectName("frame_16")
        self.verticalLayout_7.addWidget(self.frame_16)
        self.AlterarImagemdeAssinaturapushButton = QtWidgets.QPushButton(parent=self.frame_12)
        self.AlterarImagemdeAssinaturapushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.AlterarImagemdeAssinaturapushButton.setObjectName("AlterarImagemdeAssinaturapushButton")
        self.verticalLayout_7.addWidget(self.AlterarImagemdeAssinaturapushButton)
        self.gridLayout_10.addWidget(self.frame_12, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.frame_11)
        self.stackedWidget.addWidget(self.page)
        self.settings_page = QtWidgets.QWidget()
        self.settings_page.setStyleSheet("")
        self.settings_page.setObjectName("settings_page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.settings_page)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(parent=self.settings_page)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_4.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.nomeTerceiroEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.nomeTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nomeTerceiroEdit.setObjectName("nomeTerceiroEdit")
        self.verticalLayout_10.addWidget(self.nomeTerceiroEdit)
        self.contatoTerceiroEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.contatoTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.contatoTerceiroEdit.setObjectName("contatoTerceiroEdit")
        self.verticalLayout_10.addWidget(self.contatoTerceiroEdit)
        self.cidadeTerceiroEdit = QtWidgets.QLineEdit(parent=self.frame_4)
        self.cidadeTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.cidadeTerceiroEdit.setObjectName("cidadeTerceiroEdit")
        self.verticalLayout_10.addWidget(self.cidadeTerceiroEdit)
        self.cpfTerceiro = QtWidgets.QLineEdit(parent=self.frame_4)
        self.cpfTerceiro.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpfTerceiro.setObjectName("cpfTerceiro")
        self.verticalLayout_10.addWidget(self.cpfTerceiro)
        self.observacoesTerceiroEdit = QtWidgets.QTextEdit(parent=self.frame_4)
        self.observacoesTerceiroEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.observacoesTerceiroEdit.setObjectName("observacoesTerceiroEdit")
        self.verticalLayout_10.addWidget(self.observacoesTerceiroEdit)
        self.SalvarTerceiropushButton = QtWidgets.QPushButton(parent=self.frame_4)
        self.SalvarTerceiropushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.SalvarTerceiropushButton.setObjectName("SalvarTerceiropushButton")
        self.verticalLayout_10.addWidget(self.SalvarTerceiropushButton)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.frame_4)
        self.pushButton_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_10.addWidget(self.pushButton_3)
        self.gridLayout_7.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout.setObjectName("gridLayout")
        self.codChipMaeEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.codChipMaeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipMaeEdit.setObjectName("codChipMaeEdit")
        self.gridLayout.addWidget(self.codChipMaeEdit, 3, 0, 1, 1)
        self.pelagemEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.pelagemEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.pelagemEdit.setObjectName("pelagemEdit")
        self.gridLayout.addWidget(self.pelagemEdit, 3, 1, 1, 1)
        self.cpfProprietario = QtWidgets.QLineEdit(parent=self.frame_3)
        self.cpfProprietario.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpfProprietario.setObjectName("cpfProprietario")
        self.gridLayout.addWidget(self.cpfProprietario, 6, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButton_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 8, 0, 1, 1)
        self.nascimentoEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.nascimentoEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nascimentoEdit.setObjectName("nascimentoEdit")
        self.gridLayout.addWidget(self.nascimentoEdit, 2, 0, 1, 1)
        self.codChipPaiEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.codChipPaiEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipPaiEdit.setObjectName("codChipPaiEdit")
        self.gridLayout.addWidget(self.codChipPaiEdit, 4, 0, 1, 1)
        self.precoCompraEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.precoCompraEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.precoCompraEdit.setObjectName("precoCompraEdit")
        self.gridLayout.addWidget(self.precoCompraEdit, 4, 1, 1, 1)
        self.precoVendaEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.precoVendaEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.precoVendaEdit.setObjectName("precoVendaEdit")
        self.gridLayout.addWidget(self.precoVendaEdit, 5, 1, 1, 1)
        self.tipoSangueEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.tipoSangueEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.tipoSangueEdit.setObjectName("tipoSangueEdit")
        self.gridLayout.addWidget(self.tipoSangueEdit, 5, 0, 1, 1)
        self.cpfCriadorEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.cpfCriadorEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.cpfCriadorEdit.setObjectName("cpfCriadorEdit")
        self.gridLayout.addWidget(self.cpfCriadorEdit, 6, 0, 1, 1)
        self.Sexo = QtWidgets.QLineEdit(parent=self.frame_3)
        self.Sexo.setStyleSheet("color: rgb(255, 255, 255);")
        self.Sexo.setObjectName("Sexo")
        self.gridLayout.addWidget(self.Sexo, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_3.setMinimumSize(QtCore.QSize(100, 50))
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:rgb(255,255,255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)
        self.salvarAnimalpushButton = QtWidgets.QPushButton(parent=self.frame_3)
        self.salvarAnimalpushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.salvarAnimalpushButton.setObjectName("salvarAnimalpushButton")
        self.gridLayout.addWidget(self.salvarAnimalpushButton, 8, 1, 1, 1)
        self.nomeEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.nomeEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.nomeEdit.setObjectName("nomeEdit")
        self.gridLayout.addWidget(self.nomeEdit, 1, 1, 1, 1)
        self.codChipEdit = QtWidgets.QLineEdit(parent=self.frame_3)
        self.codChipEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipEdit.setObjectName("codChipEdit")
        self.gridLayout.addWidget(self.codChipEdit, 1, 0, 1, 1)
        self.foto1Animallabel = QtWidgets.QLabel(parent=self.frame_3)
        self.foto1Animallabel.setText("")
        self.foto1Animallabel.setObjectName("foto1Animallabel")
        self.gridLayout.addWidget(self.foto1Animallabel, 7, 0, 1, 1)
        self.foto2Animallabel = QtWidgets.QLabel(parent=self.frame_3)
        self.foto2Animallabel.setText("")
        self.foto2Animallabel.setObjectName("foto2Animallabel")
        self.gridLayout.addWidget(self.foto2Animallabel, 7, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_2)
        self.stackedWidget.addWidget(self.settings_page)
        self.busca = QtWidgets.QWidget()
        self.busca.setObjectName("busca")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.busca)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_6 = QtWidgets.QFrame(parent=self.busca)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame = QtWidgets.QFrame(parent=self.frame_6)
        self.frame.setMinimumSize(QtCore.QSize(650, 0))
        self.frame.setMaximumSize(QtCore.QSize(650, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.criterioBuscaComboBox = QtWidgets.QComboBox(parent=self.frame)
        self.criterioBuscaComboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 71));")
        self.criterioBuscaComboBox.setObjectName("criterioBuscaComboBox")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.criterioBuscaComboBox.addItem("")
        self.gridLayout_3.addWidget(self.criterioBuscaComboBox, 3, 0, 1, 1)
        self.buscarAnimalpushButton = QtWidgets.QPushButton(parent=self.frame)
        self.buscarAnimalpushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.buscarAnimalpushButton.setObjectName("buscarAnimalpushButton")
        self.gridLayout_3.addWidget(self.buscarAnimalpushButton, 3, 2, 1, 1)
        self.buscaDeAnimallineEdit = QtWidgets.QLineEdit(parent=self.frame)
        self.buscaDeAnimallineEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.buscaDeAnimallineEdit.setObjectName("buscaDeAnimallineEdit")
        self.gridLayout_3.addWidget(self.buscaDeAnimallineEdit, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setMinimumSize(QtCore.QSize(200, 20))
        self.label.setMaximumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.buscaDeAnimaltableWidget = QtWidgets.QTableWidget(parent=self.frame)
        self.buscaDeAnimaltableWidget.setMinimumSize(QtCore.QSize(0, 250))
        self.buscaDeAnimaltableWidget.setMaximumSize(QtCore.QSize(16777215, 250))
        self.buscaDeAnimaltableWidget.setStyleSheet("color: rgb(255, 255, 255);")
        self.buscaDeAnimaltableWidget.setObjectName("buscaDeAnimaltableWidget")
        self.buscaDeAnimaltableWidget.setColumnCount(0)
        self.buscaDeAnimaltableWidget.setRowCount(0)
        self.gridLayout_3.addWidget(self.buscaDeAnimaltableWidget, 5, 0, 1, 3)
        self.frame_9 = QtWidgets.QFrame(parent=self.frame)
        self.frame_9.setMinimumSize(QtCore.QSize(150, 100))
        self.frame_9.setMaximumSize(QtCore.QSize(1200, 50))
        self.frame_9.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.codChipMaeBuscacheckBox = QtWidgets.QCheckBox(parent=self.frame_9)
        self.codChipMaeBuscacheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipMaeBuscacheckBox.setObjectName("codChipMaeBuscacheckBox")
        self.gridLayout_5.addWidget(self.codChipMaeBuscacheckBox, 0, 1, 1, 1)
        self.pelagemBuscacheckbox = QtWidgets.QCheckBox(parent=self.frame_9)
        self.pelagemBuscacheckbox.setStyleSheet("color: rgb(255, 255, 255);")
        self.pelagemBuscacheckbox.setObjectName("pelagemBuscacheckbox")
        self.gridLayout_5.addWidget(self.pelagemBuscacheckbox, 0, 3, 1, 1)
        self.compraBuscacheckBox = QtWidgets.QCheckBox(parent=self.frame_9)
        self.compraBuscacheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.compraBuscacheckBox.setObjectName("compraBuscacheckBox")
        self.gridLayout_5.addWidget(self.compraBuscacheckBox, 1, 1, 1, 2)
        self.nascimentoBuscacheckBox = QtWidgets.QCheckBox(parent=self.frame_9)
        self.nascimentoBuscacheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.nascimentoBuscacheckBox.setObjectName("nascimentoBuscacheckBox")
        self.gridLayout_5.addWidget(self.nascimentoBuscacheckBox, 0, 0, 1, 1)
        self.codChipPaiBuscacheckBox = QtWidgets.QCheckBox(parent=self.frame_9)
        self.codChipPaiBuscacheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.codChipPaiBuscacheckBox.setObjectName("codChipPaiBuscacheckBox")
        self.gridLayout_5.addWidget(self.codChipPaiBuscacheckBox, 0, 2, 1, 1)
        self.vendaBuscacheckBox = QtWidgets.QCheckBox(parent=self.frame_9)
        self.vendaBuscacheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.vendaBuscacheckBox.setObjectName("vendaBuscacheckBox")
        self.gridLayout_5.addWidget(self.vendaBuscacheckBox, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.frame_9, 4, 0, 1, 3)
        self.horizontalLayout_8.addWidget(self.frame)
        self.frame_7 = QtWidgets.QFrame(parent=self.frame_6)
        self.frame_7.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_9 = QtWidgets.QLabel(parent=self.frame_7)
        self.label_9.setMinimumSize(QtCore.QSize(100, 40))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 3)
        self.criterioBuscaTerceirocomboBox = QtWidgets.QComboBox(parent=self.frame_7)
        self.criterioBuscaTerceirocomboBox.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(0, 0, 0, 71));")
        self.criterioBuscaTerceirocomboBox.setObjectName("criterioBuscaTerceirocomboBox")
        self.criterioBuscaTerceirocomboBox.addItem("")
        self.criterioBuscaTerceirocomboBox.addItem("")
        self.criterioBuscaTerceirocomboBox.addItem("")
        self.criterioBuscaTerceirocomboBox.addItem("")
        self.gridLayout_4.addWidget(self.criterioBuscaTerceirocomboBox, 1, 0, 1, 1)
        self.buscaTerceirolineEdit = QtWidgets.QLineEdit(parent=self.frame_7)
        self.buscaTerceirolineEdit.setStyleSheet("color: rgb(255,255,255);")
        self.buscaTerceirolineEdit.setObjectName("buscaTerceirolineEdit")
        self.gridLayout_4.addWidget(self.buscaTerceirolineEdit, 1, 1, 1, 1)
        self.buscarTerceiropushButton = QtWidgets.QPushButton(parent=self.frame_7)
        self.buscarTerceiropushButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 255, 255, 140));")
        self.buscarTerceiropushButton.setObjectName("buscarTerceiropushButton")
        self.gridLayout_4.addWidget(self.buscarTerceiropushButton, 1, 2, 1, 1)
        self.frame_10 = QtWidgets.QFrame(parent=self.frame_7)
        self.frame_10.setMinimumSize(QtCore.QSize(50, 50))
        self.frame_10.setMaximumSize(QtCore.QSize(500, 30))
        self.frame_10.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_10)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.cidadeTerceirocheckBox = QtWidgets.QCheckBox(parent=self.frame_10)
        self.cidadeTerceirocheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.cidadeTerceirocheckBox.setObjectName("cidadeTerceirocheckBox")
        self.gridLayout_6.addWidget(self.cidadeTerceirocheckBox, 0, 0, 1, 1)
        self.observacoesTerceirocheckBox = QtWidgets.QCheckBox(parent=self.frame_10)
        self.observacoesTerceirocheckBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.observacoesTerceirocheckBox.setObjectName("observacoesTerceirocheckBox")
        self.gridLayout_6.addWidget(self.observacoesTerceirocheckBox, 0, 1, 1, 1)
        self.gridLayout_4.addWidget(self.frame_10, 2, 0, 1, 3)
        self.tableView = QtWidgets.QTableView(parent=self.frame_7)
        self.tableView.setMinimumSize(QtCore.QSize(0, 250))
        self.tableView.setMaximumSize(QtCore.QSize(16777215, 250))
        self.tableView.setObjectName("tableView")
        self.gridLayout_4.addWidget(self.tableView, 3, 0, 1, 3)
        self.horizontalLayout_8.addWidget(self.frame_7)
        self.verticalLayout_12.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.busca)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.center_main_items)
        self.verticalLayout.addWidget(self.main_body)
        self.main_footer = QtWidgets.QFrame(parent=self.centralwidget)
        self.main_footer.setMinimumSize(QtCore.QSize(0, 50))
        self.main_footer.setMaximumSize(QtCore.QSize(16777215, 30))
        self.main_footer.setStyleSheet("QFrame{\n"
"    background-color: rgb(0, 0, 0);\n"
"    border-top-color: solid 1px  rgb(0, 0, 0);\n"
"}\n"
"QLabel{\n"
"    color: #fff;\n"
"}")
        self.main_footer.setFrameShape(QtWidgets.QFrame.Shape.WinPanel)
        self.main_footer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.main_footer.setObjectName("main_footer")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.main_footer)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(parent=self.main_footer)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.size_grip = QtWidgets.QFrame(parent=self.main_footer)
        self.size_grip.setMinimumSize(QtCore.QSize(20, 20))
        self.size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.size_grip.setStyleSheet("")
        self.size_grip.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_6.addWidget(self.size_grip, 0, QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignBottom)
        self.verticalLayout.addWidget(self.main_footer)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Painel Administrativo"))
        self.label_13.setText(_translate("MainWindow", "Importação de Animais"))
        self.arquivo.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.importarAnimaispushButton.setText(_translate("MainWindow", "Importar!"))
        self.tipoImportacaoAnimaiscomboBox.setItemText(0, _translate("MainWindow", "Somente Cadastros Novos"))
        self.tipoImportacaoAnimaiscomboBox.setItemText(1, _translate("MainWindow", "Cadastros de Atualização"))
        self.escolherArquivoImportacaoAnaimaispushButton.setText(_translate("MainWindow", "Arquivo"))
        self.esclhoerArquivoImportacaoTerceiropushButton.setText(_translate("MainWindow", "Arquivo"))
        self.tipoImportacaoTerceirocomboBox.setItemText(0, _translate("MainWindow", "Somente Cadastros Novos"))
        self.tipoImportacaoTerceirocomboBox.setItemText(1, _translate("MainWindow", "Cadastros de Atualização"))
        self.lineEdit_11.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.importarTerceirospushButton.setText(_translate("MainWindow", "Importar!"))
        self.label_14.setText(_translate("MainWindow", "Importação de Terceiros"))
        self.label_11.setText(_translate("MainWindow", "Importação de Dados"))
        self.backupSeguranapushButton.setText(_translate("MainWindow", "Backup Segurança"))
        self.label_12.setText(_translate("MainWindow", "Gerenciar Dados"))
        self.backupAssocialpushButton.setText(_translate("MainWindow", "Backup Associação"))
        self.selectMainDirpushButton.setText(_translate("MainWindow", "Diretorio de Dados"))
        self.nomePerfilAcessolineEdit.setPlaceholderText(_translate("MainWindow", "Nome"))
        self.cpfPerfilAcessolineEdit.setPlaceholderText(_translate("MainWindow", "Nome Empresarial"))
        self.nascimentoPerfilAcessolineEdit.setPlaceholderText(_translate("MainWindow", "Nascimento"))
        self.senhaPerfilAcessocheckBox.setText(_translate("MainWindow", "Sem-Senha"))
        self.cpfOuCnpjPerfilAcessolineEdit.setPlaceholderText(_translate("MainWindow", "CPF ou CNPJ"))
        self.cpfPerfilAcessolineEdit_2.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.alterarAcessosPerfilAcessospushButton.setText(_translate("MainWindow", "Alterar Acessos"))
        self.senhaPerfilAcessolineEdit.setText(_translate("MainWindow", "Senha"))
        self.senhaPerfilAcessolineEdit.setPlaceholderText(_translate("MainWindow", "Nome Empresarial"))
        self.nomeUsuarioPerfilAcessolineEdit.setText(_translate("MainWindow", "Nome de Usuario"))
        self.nomeUsuarioPerfilAcessolineEdit.setPlaceholderText(_translate("MainWindow", "Nome Empresarial"))
        self.criadorPerfilAcessocheckBox.setText(_translate("MainWindow", "Criador"))
        self.label_10.setText(_translate("MainWindow", "Perfil de Acesso"))
        self.label_4.setText(_translate("MainWindow", "Imagem de Assinatura"))
        self.AlterarImagemdeAssinaturapushButton.setText(_translate("MainWindow", "Alterar Imagem de Assinatura"))
        self.label_8.setText(_translate("MainWindow", "Cadastrar Novo Terceiro"))
        self.nomeTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Nome Completo"))
        self.contatoTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Contatos"))
        self.cidadeTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Cidade"))
        self.cpfTerceiro.setPlaceholderText(_translate("MainWindow", "CPF "))
        self.observacoesTerceiroEdit.setPlaceholderText(_translate("MainWindow", "Observações Gerais"))
        self.SalvarTerceiropushButton.setText(_translate("MainWindow", "Salvar"))
        self.pushButton_3.setText(_translate("MainWindow", "Excluir"))
        self.codChipMaeEdit.setPlaceholderText(_translate("MainWindow", "Codigo do Chip Mae"))
        self.pelagemEdit.setPlaceholderText(_translate("MainWindow", "Pelagem"))
        self.cpfProprietario.setPlaceholderText(_translate("MainWindow", "CPF do Criador"))
        self.pushButton_2.setText(_translate("MainWindow", "Excluir"))
        self.nascimentoEdit.setPlaceholderText(_translate("MainWindow", "Nascimento"))
        self.codChipPaiEdit.setPlaceholderText(_translate("MainWindow", "Codigo do Chip Pai"))
        self.precoCompraEdit.setPlaceholderText(_translate("MainWindow", "Preço de Compra"))
        self.precoVendaEdit.setPlaceholderText(_translate("MainWindow", "Preço de Venda"))
        self.tipoSangueEdit.setPlaceholderText(_translate("MainWindow", "Tipo Sanguineo"))
        self.cpfCriadorEdit.setPlaceholderText(_translate("MainWindow", "CPF do Criador"))
        self.Sexo.setPlaceholderText(_translate("MainWindow", "Digite Feminino ou Masculuno"))
        self.label_3.setText(_translate("MainWindow", "Cadastrar e Alteraçao de Animais"))
        self.salvarAnimalpushButton.setText(_translate("MainWindow", "Salvar"))
        self.nomeEdit.setPlaceholderText(_translate("MainWindow", "Nome do Animal"))
        self.codChipEdit.setPlaceholderText(_translate("MainWindow", "Codigo do Chip"))
        self.criterioBuscaComboBox.setPlaceholderText(_translate("MainWindow", "Criterio"))
        self.criterioBuscaComboBox.setItemText(0, _translate("MainWindow", "Chip"))
        self.criterioBuscaComboBox.setItemText(1, _translate("MainWindow", "ChipPai"))
        self.criterioBuscaComboBox.setItemText(2, _translate("MainWindow", "ChipMae"))
        self.criterioBuscaComboBox.setItemText(3, _translate("MainWindow", "Nascimento"))
        self.criterioBuscaComboBox.setItemText(4, _translate("MainWindow", "Nome"))
        self.criterioBuscaComboBox.setItemText(5, _translate("MainWindow", "Pelagem"))
        self.criterioBuscaComboBox.setItemText(6, _translate("MainWindow", "Proprietario"))
        self.criterioBuscaComboBox.setItemText(7, _translate("MainWindow", "Preço de Compra"))
        self.criterioBuscaComboBox.setItemText(8, _translate("MainWindow", "Preço de Venda"))
        self.buscarAnimalpushButton.setText(_translate("MainWindow", "Buscar"))
        self.buscaDeAnimallineEdit.setPlaceholderText(_translate("MainWindow", "Digite aqui a sua busca"))
        self.label.setText(_translate("MainWindow", "Busca de Animais"))
        self.codChipMaeBuscacheckBox.setText(_translate("MainWindow", "Mãe"))
        self.pelagemBuscacheckbox.setText(_translate("MainWindow", "Pelagem"))
        self.compraBuscacheckBox.setText(_translate("MainWindow", "Compra"))
        self.nascimentoBuscacheckBox.setText(_translate("MainWindow", "Nasc"))
        self.codChipPaiBuscacheckBox.setText(_translate("MainWindow", "Pai"))
        self.vendaBuscacheckBox.setText(_translate("MainWindow", "Venda"))
        self.label_9.setText(_translate("MainWindow", "Busca de Terceiros"))
        self.criterioBuscaTerceirocomboBox.setItemText(0, _translate("MainWindow", "Criterio"))
        self.criterioBuscaTerceirocomboBox.setItemText(1, _translate("MainWindow", "CPF"))
        self.criterioBuscaTerceirocomboBox.setItemText(2, _translate("MainWindow", "Contato"))
        self.criterioBuscaTerceirocomboBox.setItemText(3, _translate("MainWindow", "Nome"))
        self.buscaTerceirolineEdit.setPlaceholderText(_translate("MainWindow", "Digite aqui"))
        self.buscarTerceiropushButton.setText(_translate("MainWindow", "Buscar"))
        self.cidadeTerceirocheckBox.setText(_translate("MainWindow", "Cidade"))
        self.observacoesTerceirocheckBox.setText(_translate("MainWindow", "Observações"))
        self.label_7.setText(_translate("MainWindow", "v 1.0"))

        
        
        
        #Inicio das atribuições de ação
        self.image_path1 = ""
        self.image_path2 = ""
        self.foto1Animallabel.mousePressEvent = self.setFotoAnimal1
        self.foto2Animallabel.mousePressEvent = self.setFotoAnimal2
        self.selectMainDirpushButton.clicked.connect(self.select_or_create_directory)
        self.cadastrospushButton.clicked.connect(self.goToAnimaisCadastro)
        self.configuracoespushButton.clicked.connect(self.goToConfiguracoes)
        self.buscasPushButton.clicked.connect(self.goToRelatorios)
        self.closeButton.clicked.connect(QApplication.quit)
        self.salvarAnimalpushButton.clicked.connect(self.salvarAnimais)
        self.SalvarTerceiropushButton.clicked.connect(self.salvarTerceiro)
        self.buscarAnimalpushButton.clicked.connect(self.resultadoBuscaAnimais)
        self.buscaDeAnimaltableWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.buscaDeAnimaltableWidget.customContextMenuRequested.connect(self.rigthClickBuscaAnimais)


    def goToAnimaisCadastro(self):
        self.stackedWidget.setCurrentIndex(2)
    
    def goToRelatorios(self):
        self.stackedWidget.setCurrentIndex(0)

    def goToConfiguracoes(self):
        self.stackedWidget.setCurrentIndex(1)


    def salvarAnimais(self):
        print("Criando ou Salvando Animal")
        #checkagem de campos
        if self.codChipEdit.text() == "":
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("Codigo de Chip do Animal é obrigatorio")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        if self.nomeEdit.text() == "":
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("O Nome do Animal é obrigatorio")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        if self.nascimentoEdit.text() == "":
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("A data de Nascimento é obrigatoria")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        print(self.Sexo.text(), "here")
        if  not (self.Sexo.text() == "Macho" or self.Sexo.text() == "Femea") :
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("O Sexo so pode ser preenchido pelas palavras 'Macho' ou 'Femea'")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        
        if self.pelagemEdit.text() == "":
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("A Pelagem é Obrigatoria")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        if self.tipoSangueEdit.text() == "" :
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("O tipo Sanquineo é Obrigatorio")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        if self.cpfCriadorEdit.text() == "" :
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("O CPF do Criador é Obrigatorio")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return
        
        if self.cpfProprietario.text() == "" :
            messageBox = QtWidgets.QMessageBox()
            messageBox.setText("O CPF do Proprietário do Animal é Obrigatorio")
            messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
            messageBox.exec()
            return

        if self.image_path1: 
            img1 = Image.open(self.image_path1)
            img1.save(self.personalDir+f"\\ImagensDeAnimais\\fot1_{self.codChipEdit.text()}.png")
            path1 = self.personalDir+f"\\ImagensDeAnimais\\fot1_{self.codChipEdit.text()}.png"
        else:
            path1 = "" #colocar imagem padrao
        
        if self.image_path2:
            img2 = Image.open(self.image_path2)
            img2.save(self.personalDir+f"\\ImagensDeAnimais\\fot2_{self.codChipEdit.text()}.png")
            path2 = self.personalDir+f"\\ImagensDeAnimais\\fot2_{self.codChipEdit.text()}.png"
        else:
            path2 = "" #colocar ImagemPadrao
        
        #checkagem se o codAnimal ja existe, se existe faz um update, se não existe cadastra novo animal
        try:
            conn = sqlite3.connect(self.mainDatabasePath)
            cursor = conn.cursor()
            result = cursor.execute(f"SELECT nomeAnimal FROM animais_data WHERE codChip='{self.codChipEdit.text()}'").fetchone()
            if result:
                print("Já existe, fazer update")
                queryToInsertData = f''' UPDATE animais_data SET nomeAnimal = '{self.nomeEdit.text()}', new_sexoAnimal = '{self.Sexo.text()}', nascimento = '{self.nascimentoEdit.text()}', pelagem = '{self.pelagemEdit.text()}', preco_compra = '{self.precoCompraEdit.text()}', preco_venda = '{self.precoVendaEdit.text()}', cpfProprietario = '{self.cpfProprietario.text()}', cpfCriador = '{self.cpfCriadorEdit.text()}', tipoSanquineo = '{self.tipoSangueEdit.text()}', fot1 = '{path1}', fot2 = '{path2}' WHERE codChip = {self.codChipEdit.text()} '''
                print(queryToInsertData)
                cursor.execute(queryToInsertData)
                conn.commit()
                messageBox = QtWidgets.QMessageBox()
                messageBox.setText("Dados Alterados com Sucesso!")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                messageBox.exec()
                self.setupUi(self.MainWindow, self.mainDir, self.personalDir)
            else:
                queryToInsertData = f'''INSERT INTO animais_data (codChip,  new_sexoAnimal, nomeAnimal, nascimento, CodChipMae, codChipPai, pelagem, preco_compra, preco_venda, cpfProprietario, cpfCriador, tipoSanquineo, fot1, fot2 ) VALUES 
                ( '{self.codChipEdit.text()}' , '{self.Sexo.text()}','{self.nomeEdit.text()}', '{self.nascimentoEdit.text()}', '{self.codChipMaeEdit.text()}', '{self.codChipPaiEdit.text()}', '{self.pelagemEdit.text()}', '{self.precoCompraEdit.text()}', '{self.precoVendaEdit.text()}', '{self.cpfProprietario.text()}', '{self.cpfCriadorEdit.text()}', '{self.tipoSangueEdit.text()}', '{self.image_path1}', '{self.image_path2}')'''
                cursor.execute(queryToInsertData)
                conn.commit()
                messageBox = QtWidgets.QMessageBox()
                messageBox.setText("Novo Animal Cadastrado com Sucesso")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                messageBox.exec()
                self.setupUi(self.MainWindow, self.mainDir, self.personalDir)
            conn.close()
            return
        except sqlite3.Error as e: 
            print(str(e))
    
    def salvarTerceiro(self):
        print("Salvando Terceiro")
        #saveCommandSql =f'''INSERT INTO terceiros_data (cpfTerceiro, nomeTerceiro, contatoTerceiro, cidadeTerceiro, observacaoTerceiro ) VALUES ('{self.cpfTerceiroEdit.text()}', '{self.nomeTerceiroEdit.text()}', '{self.contatoTerceiroEdit.text()}','{self.cidadeTerceiroEdit.text()}', '{self.observacoesTerceiroEdit.toPlainText()}')'''
        #print({self.cpfTerceiroEdit.text()}, {self.nomeTerceiroEdit.text()}, {self.contatoTerceiroEdit.text()}, {self.cidadeTerceiroEdit.text()}, {self.observacoesTerceiroEdit.toPlainText()})
        #try:
           # print(self.mainDatabasePath)
       #     connection = sqlite3.connect(self.mainDatabasePath)
        #    cursor = connection.cursor()
        #    cursor.execute(saveCommandSql)
        #    connection.commit()
        #    connection.close()
        #    
        #except sqlite3.Error as e:
        #    print(str(e))
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText("Função já codificada, falta copiar para codigo")
        messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
        messageBox.exec()

    def resultadoBuscaAnimais(self):
        strdeBusca = self.buscaDeAnimallineEdit.text()
        searchInDb = "codChip cpfProprietario cpfCriador"
        headerTitle = ["Chip", "Proprietário", "Criador"]
        #codChip, cpfprorietario, cpfCriador já estao por default na busca e exibiçao de dados.
        if self.nascimentoBuscacheckBox.isChecked():
            searchInDb += " nascimento"
            headerTitle.append("Nascimento")
        if self.codChipMaeBuscacheckBox.isChecked():
            searchInDb +=" codChipMae"
            headerTitle.append("Mãe")
        if self.codChipPaiBuscacheckBox.isChecked():
            searchInDb +=" codChipPai"
            headerTitle.append("Pai")
        if self.pelagemBuscacheckbox.isChecked():
            searchInDb +=" pelagem"
            headerTitle.append("Pelagem")
        if self.vendaBuscacheckBox.isChecked():
            searchInDb.join(" preco_venda")
            headerTitle.append("Venda")
        if self.compraBuscacheckBox.isChecked():
            searchInDb +=" preco_compra"
            headerTitle.append("Compra")
        
        criterioSelected = self.criterioBuscaComboBox.currentText()
        if criterioSelected == "Chip":
            criterio = "codChip"
        elif criterioSelected == "ChipPai":
            criterio = "codChipPai"
        elif criterioSelected == "ChipMae":
            criterio = "codChipMae"
        elif criterioSelected == "Nascimento":
            criterio = "nascimento"
        elif criterioSelected == "Nome":
            criterio = "nomeAnimal"
        elif criterioSelected == "Pelagem":
            criterio = "pelagem"
        elif criterioSelected == "Proprietario":
            criterio = "cpfProprietario"
        elif criterioSelected == "Criador":
            criterio = "cpfCriador"
        elif criterioSelected == "Tipo Sanguineo":
            criterio = "tipoSanquineo"
        else:
            return

        columns = searchInDb.split(" ")
        buscasql =f'''SELECT {', '.join(columns)} FROM animais_data WHERE  {criterio}={strdeBusca}'''
        print(buscasql)
        self.buscaDeAnimaltableWidget.clearContents()
        self.buscaDeAnimaltableWidget.setRowCount(0)
        try:
            connection = sqlite3.connect(self.mainDatabasePath)
            cursor = connection.cursor()
            cursor.execute(buscasql)
            connection.commit()
            rows = cursor.fetchall()
            connection.close()
            print(len(rows))
            if len(rows) == 0: 
                messageBox = QtWidgets.QMessageBox()
                messageBox.setText("Nenhum Animal encontrado! Tente Novamente")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                messageBox.exec()
                return            
            self.buscaDeAnimaltableWidget.setRowCount(20)  # Set the number of rows as needed
            print(print(columns))
            self.buscaDeAnimaltableWidget.setColumnCount(8)
            rows.insert(0, tuple(headerTitle))
            self.buscaDeAnimaltableWidget.horizontalHeader().setVisible(False)
            self.buscaDeAnimaltableWidget.verticalHeader().setVisible(False)
            # Set the column headers (optional)

            # Populate the QTableWidget with data            
            for row_number, row_data in enumerate(rows):
                self.buscaDeAnimaltableWidget.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(data))
                    self.buscaDeAnimaltableWidget.setItem(row_number, column_number, item)
            self.buscaDeAnimaltableWidget.resizeColumnsToContents()
                
        except sqlite3.Error as e:
            print(str(e), "Erro da busca")

        
    def rigthClickBuscaAnimais(self, event):
        contextMenu = QtWidgets.QMenu(self.buscaDeAnimaltableWidget)
        actionExcluir = QtGui.QAction("Excluir")
        actionAlterar = QtGui.QAction("Alterar")
        actionGenealogia = QtGui.QAction("Genealogia")

        actionExcluir.triggered.connect(self.actionExcluir)
        actionAlterar.triggered.connect(self.actionAlterar)
        actionGenealogia.triggered.connect(self.genealogia)

        contextMenu.addAction(actionExcluir)
        contextMenu.addAction(actionAlterar)
        contextMenu.addAction(actionGenealogia)

        contextMenu.exec(self.buscaDeAnimaltableWidget.mapToGlobal(QtCore.QPoint(event.x(), event.y())))

    def genealogia(self):
        print("Gerar Genealogia")
        selected_item = self.buscaDeAnimaltableWidget.selectedItems()
        #ajustar erros. 
        row = selected_item[0].row()
        chipCodeAnimal = self.buscaDeAnimaltableWidget.item(row, 0).text()
        #criando diretorios
        if os.path.exists(self.personalDir+f"\\Genealogias\\{chipCodeAnimal}"):
            shutil.rmtree(self.personalDir+f"\\Genealogias\\{chipCodeAnimal}")

        os.makedirs(self.personalDir+f"\\Genealogias\\{chipCodeAnimal}")
        MakeGenealogy.tableToImageAnimal(self.mainDatabasePath, self.personalDir+f"\\Genealogias\\{chipCodeAnimal}", str(chipCodeAnimal))
        #pegando toda genealogia do Animal
        codAllRelatives = MakeGenealogy.getAllRelativies(self.mainDatabasePath, str(chipCodeAnimal))
        print(len(codAllRelatives))

        #create imgtables to all relativies
        for i in range(1, 15):
            MakeGenealogy.tableToImageRelativies(self.mainDatabasePath, self.personalDir+f"\\Genealogias\\{chipCodeAnimal}", str(codAllRelatives[i][0]), str(codAllRelatives[i][1]))
        #create graph
        MakeGenealogy.createGenealogyImage(self.personalDir+f"\\Genealogias\\{chipCodeAnimal}")

        QApplication.quit()

    def actionExcluir(self):
        selected_item = self.buscaDeAnimaltableWidget.selectedItems()
        if selected_item:
            row = selected_item[0].row()
            chipCodeAnimal = self.buscaDeAnimaltableWidget.item(row, 0).text()
            print(chipCodeAnimal)
            response = QtWidgets.QMessageBox.question(self.MainWindow, "Essa operação é Irreversivel", "Podemos continuar?", QtWidgets.QMessageBox.StandardButton.Yes | QtWidgets.QMessageBox.StandardButton.No)

            if response == QtWidgets.QMessageBox.StandardButton.No:
                print("Nao Concluimos")
            else:
            #colocar mensage box para que usuario confire a exclusão do animal
                connection = sqlite3.connect(self.mainDatabasePath)
                cursor = connection.cursor()
                sqlcommand = f'''DELETE FROM animais_data WHERE codChip = '{chipCodeAnimal}' '''
                cursor.execute(sqlcommand)
                connection.commit()
                connection.close()
                messageBox = QtWidgets.QMessageBox()
                messageBox.setText("Animal Excluido com Sucesso! Essa operação é Irreversivel")
                messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
                messageBox.exec()
                self.setupUi(self.MainWindow, self.mainDir, self.personalDir)
    
    def select_or_create_directory(self):
       dir = QtWidgets.QFileDialog.getExistingDirectory(self.centralwidget, "Selecione ou Crie um Diretorio")
       print(dir)
       messageBox = QtWidgets.QMessageBox()
       messageBox.setText("Função já codificada, falta copiar para codigo")
       messageBox.setStandardButtons(QtWidgets.QMessageBox.StandardButton.Ok)
       messageBox.exec()
        

    def setFotoAnimal1(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            options = QtWidgets.QFileDialog.Option.ReadOnly
            self.image_path1, _ = QtWidgets.QFileDialog.getOpenFileName(self.foto1Animallabel, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.ico *.tiff)", options=options)
            if self.image_path1:
                pixmap = QtGui.QPixmap(self.image_path1)
                if not pixmap.isNull():
                    self.foto1Animallabel.setPixmap(pixmap.scaled(self.foto1Animallabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
        
    def setFotoAnimal2(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            options = QtWidgets.QFileDialog.Option.ReadOnly
            self.image_path2, _ = QtWidgets.QFileDialog.getOpenFileName(self.foto2Animallabel, "Select Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.ico *.tiff)", options=options)
            if self.image_path2:
                pixmap = QtGui.QPixmap(self.image_path2)
                if not pixmap.isNull():
                    self.foto2Animallabel.setPixmap(pixmap.scaled(self.foto2Animallabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))


    def actionAlterar(self):
        #precisa ir antes para a tela de dados, então ele precisa setar o currente index e preencher os campos:
        self.stackedWidget.setCurrentIndex(1) #vai para area de cadastro
        selected_item = self.buscaDeAnimaltableWidget.selectedItems()
        if selected_item:
            row = selected_item[0].row()
            chipCodeAnimal = self.buscaDeAnimaltableWidget.item(row, 0).text()
            print(chipCodeAnimal)
        #preenche os campos com os dados pegos da row, melhor pegar o codChip e o restante dos dados num fetechone.
        try:
            conn = sqlite3.connect(self.mainDatabasePath)
            cursor = conn.cursor()
            query = f''' SELECT nomeAnimal, nascimento, CodChipMae, codChipPai, pelagem, preco_compra, preco_venda, cpfProprietario, cpfCriador, tipoSanquineo, fot1, fot2, new_sexoAnimal FROM animais_data WHERE codChip={chipCodeAnimal}'''
            cursor.execute(query)
            resultado = cursor.execute(query).fetchone()
            conn.close()

            self.codChipEdit.setText(chipCodeAnimal)
            self.nomeEdit.setText(resultado[0])
            self.nascimentoEdit.setText(resultado[1])
            self.codChipMaeEdit.setText(resultado[2])
            self.codChipPaiEdit.setText(resultado[3])
            self.pelagemEdit.setText(resultado[4])
            self.precoCompraEdit.setText(str(resultado[5]))
            self.precoVendaEdit.setText(str(resultado[6]))
            self.cpfProprietario.setText(resultado[7])
            self.cpfCriadorEdit.setText(resultado[8])
            self.tipoSangueEdit.setText(resultado[9])

            if resultado[10]:
                self.image_path1 = resultado[10]
                pixmap = QtGui.QPixmap(resultado[10])
                if not pixmap.isNull():
                    self.foto1Animallabel.setPixmap(pixmap.scaled(self.foto1Animallabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

            if resultado[11]:
                self.image_path2 = resultado[11]
                pixmap = QtGui.QPixmap(resultado[11])
                if not pixmap.isNull():
                    self.foto2Animallabel.setPixmap(pixmap.scaled(self.foto2Animallabel.size(), Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))
            
            self.Sexo.setText(resultado[12])

        except sqlite3.Error as e:
            print(str(e), " Erro de alteração de dados na busca SQL")
