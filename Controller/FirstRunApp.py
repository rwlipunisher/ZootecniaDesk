#imports here
from Views import *
from Models import *
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets


import time
import os

#from ZootecniaCLHDesktop.settings import ROOT_DIR

class FirstRunSoftware(InitDataBase, ):

    def __init__(self, app: QApplication) -> None:
        self.splash = SplashScreen()
        self.app = app
        self.viewSelected = None
    
    def runCheckList(self) -> QMainWindow:
        self.splash.show()
        self.splash.show_message("Inicialização do Sistema ...")
        time.sleep(2)
        ui = None
        #Checagem da existencia do banco de dados, se não existe ele cria
        if self._checkDataBaseExistenceOrCreatIt(self.splash):
            #o banco de dados foi criado ou detectado e esta pronto pra uso
            self.splash.show_message("Validando Chave de Acesso ... ")
            if self.__validadeToken():
                #o token esta ativo e é valido no banco de dados
                #self.viewSelected = Ui_MainWindow()
                pass
            else:
                #o token nao é valido ou nao esta no banco de dados e o sistema esta inativo
                ui = WindowInitialUserActivation()
        else:
            self.viewSelected = ViewErrorSystemRestart()
        self.splash.close()
        returnWindow = QtWidgets.QMainWindow()
        ui.setupUi(returnWindow)
        return returnWindow 

    def _checkDataBaseExistenceOrCreatIt(self, splash: SplashScreen) -> bool:
        if os.path.exists(self._pathDatabase):
            splash.show_message("Banco de dados Detectado!")
            return True
        else:
            splash.show_message("Criando Banco de Dados ...")
            return self._createDatabase()
    
    @staticmethod
    def checkTokenCPF(token: str, cpf: str ) -> bool:
        if len(token) != 10:
            return False
        else:
            if cpf != 10:
                return False
        return True