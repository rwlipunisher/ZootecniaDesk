#imports here
import os
from Models import InitDataBase


class ToolsControllsInitialSettings():
   
   @staticmethod
   def checkCpfAndToken(toke, cpf):
       return True

   @staticmethod
   def checkDataBaseExistenceOrCreatIt() -> bool:
        if os.path.exists(InitDataBase.pathDatabase):
            return True
        else:
            return InitDataBase.createDatabase()
   @staticmethod
   def checkCpf(cpf: str ) -> bool:
       # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11:
            return False

        # Calcula o primeiro dígito verificador
        soma = 0
        for i in range(9):
            soma += int(cpf[i]) * (10 - i)
        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        # Verifica se o primeiro dígito verificador está correto
        if int(cpf[9]) != digito1:
            return False

        # Calcula o segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += int(cpf[i]) * (11 - i)
        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto

        # Verifica se o segundo dígito verificador está correto
        if int(cpf[10]) != digito2:
            return False

        return True
       
   @staticmethod
   def checkToken(token: str ) -> bool:
       if len(token) != 11:
          return False
       else: 
           return True
       
   @staticmethod
   def checkInitialSettings(nome: str, nascimento: str, usuario: str, senha: str, checsenha: bool, nomeEmpresa: str, cpfOrCnpj: str):
        if nome == "":
            return False
        if nascimento == "":
            return False
        if usuario == "":
            return False
        if checsenha:
            if senha == "":
                return False
        if nomeEmpresa == "":
            return False
        if not ToolsControllsInitialSettings.checkCpf(cpfOrCnpj):
            if not ToolsControllsInitialSettings.checkCNPJ(cpfOrCnpj):
                return False
        return True
        

   @staticmethod
   def passWordcheck():
        pass

   @staticmethod
   def dataFilds():
        pass

 