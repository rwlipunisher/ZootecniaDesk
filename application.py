#index da Aplicação
from PyQt6.QtWidgets import QApplication
from Views import *
from PyQt6 import QtWidgets
import os
import sqlite3
#from ZootecniaCLHDesktop.settings import ROOT_DIR

import sys

def newMainWindow(Qmain):
     pass


if __name__ == "__main__":
     #mainDir = os.path.dirname(sys.executable)
     #mainDir = os.path.dirname(__file__).replace("\\", "/")
     mainDir = os.path.dirname(os.path.abspath(__file__))
     #criando e checkando diretorios do sistema
     
     app = QApplication(sys.argv)
     splashScreen = SplashScreen(mainDir)
     splashScreen.show()
     mainWindowApp = QtWidgets.QMainWindow()
     InterfaceInit = InitUserInterfaces(mainWindowApp, str(mainDir))
     #InterfaceGeneral = GeralInterface(mainWindowApp, str(mainDir))

     db_path = os.path.join(mainDir+ "\Resources\DataBase\main.db")

     try:
          splashScreen.show_message("Iniciando Sistema ... ")
          connection = sqlite3.connect(str(db_path))
          cursor = connection.cursor()
          consulta = "SELECT cpf, sem_senha FROM user_access_data WHERE id=1"
          cursor.execute(consulta)
          resultado = cursor.fetchone()
          cpf, sem_senha = resultado
          connection.close()
          print(cpf)
          if cpf != "000":
               if not sem_senha:
                    print("general charge")
                    splashScreen.show_message("Bem vindo!")
                    time.sleep(2)
                    splashScreen.close()
                    #vai pra pagina principal
                    del InterfaceInit
                    InterfaceInit = MainWindowApp()
                    InterfaceInit.setupUi(mainWindowApp, mainDir)
                    mainWindowApp.show()
               else:
                    splashScreen.show_message("Login!")
                    splashScreen.close()
                    InterfaceInit.loginUi()                    
          else: 
               splashScreen.show_message("Bem vindo!")
               splashScreen.close()
               InterfaceInit.tokenCpfInitUi()         

     except sqlite3.Error as e:
          #so entra aqui se der erro na leitura inicial no bamco de dados, 
          #apagar essa parte quando finalizar o codigo
          print('foqui')
          create_table_sql = """
          CREATE TABLE IF NOT EXISTS user_access_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT CHECK(length(name) <= 30),
            cpf TEXT NOT NULL,
            nascimento DATE,
            user_name TEXT CHECK(length(user_name) >= 4),
            nomeEmpresa TEXT CHECK(length(nomeEmpresa) <= 30),
            cpfOrCnpj TEXT CHECK(length(cpfOrCnpj) <= 14),
            senha TEXT,
            sem_senha BOOLEAN,
            criador BOOLEAN,
            token TEXT
          );
          """
          cursor = connection.cursor()
          cursor.execute(create_table_sql)
          connection.commit()
          insert_sql = "INSERT INTO user_access_data (cpf) VALUES (?)"
          cursor.execute(insert_sql, ("000", ))
          connection.commit()
          connection.close()
          print(str(e)) 
     

     sys.exit(app.exec())