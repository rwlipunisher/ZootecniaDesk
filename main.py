#index da Aplicação

from Controller import FirstRunSoftware
from PyQt6.QtWidgets import QApplication
from Views import *
from PyQt6 import QtWidgets
import os
#from ZootecniaCLHDesktop.settings import ROOT_DIR

import sys

def newMainWindow(Qmain):
     pass


if __name__ == "__main__":
     mainDir = os.path.dirname(__file__).replace("\\", "/")
     app = QApplication(sys.argv)
     splashScreen = SplashScreen()
     splashScreen.show()

     '''if FirstRunSoftware.checkDataBaseExistenceOrCreatIt():
            splashScreen.show_message("Banco de dados .... OK!")
            time.sleep(1)
            #o banco de dados foi criado ou detectado e esta pronto pra uso
            if 1==2: #Faz a checagem se o token existe no banco de dados e é valido
                #o token esta ativo e é valido no banco de dados
                #self.viewSelected = Ui_MainWindow()
                pass
            else:
                #o token nao é valido ou nao esta no banco de dados e o sistema não esta ativado
                splashScreen.show_message("Token Incorreto ... Exit!")
               # ui = WindowInitialUserActivation()
     else:
          viewSelected = ViewErrorSystemRestart()'''
     splashScreen.close()
     mainWindowApp = QtWidgets.QMainWindow()
     Interface = InitUserInterfaces(mainWindowApp, str(mainDir))
     Interface.tokenCpfInitUi()
     
     sys.exit(app.exec())
     
     #vai chamar MidlleController para gerenciar operacoes voltadas ao uso
     #do software
    # Create and display the initial views