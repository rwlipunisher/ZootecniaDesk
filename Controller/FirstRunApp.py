#imports here
from Views import *
from Models import *
from PyQt6.QtWidgets import QApplication

import os

#from ZootecniaCLHDesktop.settings import ROOT_DIR

class FirstRunSoftware(InitDataBase):

    def __init__(self, app: QApplication) -> None:
        self.splash = SplashScreen()
        self.app = app
        self.viewSelected = None
    
    '''def runCheckList(self) -> QMainWindow:
        self.splash.show()
        self.splash.show_message("Inicialização do Sistema ...")
        time.sleep(2)
        ui = None
        #Checagem da existencia do banco de dados, se não existe ele cria

        if self.checkDataBaseExistenceOrCreatIt():
            #o banco de dados foi criado ou detectado e esta pronto pra uso
            self.splash.show_message("Validando Chave de Acesso ... ")
            if 1==2:
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
        ui = WindowInitialUserActivation()
        ui.setupUi(returnWindow)
        return returnWindow 
    '''
   
   
    @staticmethod
    def checkCpfAndToken(toke, cpf):
        return True

    @staticmethod
    def checkDataBaseExistenceOrCreatIt() -> bool:
        if os.path.exists(InitDataBase.pathDatabase):
            return True
        else:
            return InitDataBase.createDatabase()
        
    
    
    