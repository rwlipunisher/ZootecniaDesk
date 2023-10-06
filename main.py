#index da Aplicação

from Controller import FirstRunSoftware
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets
import os
#from ZootecniaCLHDesktop.settings import ROOT_DIR

import sys

if __name__ == "__main__":
     app = QApplication(sys.argv)
     initializeApp = FirstRunSoftware(app)
     actualWindow = initializeApp.runCheckList()
     #vai chamar MidlleController para gerenciar operacoes voltadas ao uso
     #do software
     actualWindow.show()
     sys.exit(app.exec())
    # Create and display the initial views