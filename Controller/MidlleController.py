#imports here
import os
import sqlite3
from Models import InitDataBase
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx



class ToolsControllsInitialSettings:
   
   @staticmethod
   def checkCnpj(cnpj):
        # Remove caracteres não numéricos
        # Verifica se a string tem 14 dígitos
        if len(cnpj) != 14:
            return False

        # Calcula o primeiro dígito verificador
        soma = 0
        peso = 5
        for i in range(12):
            soma += int(cnpj[i]) * peso
            peso -= 1
            if peso < 2:
                peso = 9

        resto = soma % 11
        if resto < 2:
            digito1 = 0
        else:
            digito1 = 11 - resto

        # Calcula o segundo dígito verificador
        soma = 0
        peso = 6
        for i in range(13):
            soma += int(cnpj[i]) * peso
            peso -= 1
            if peso < 2:
                peso = 9

        resto = soma % 11
        if resto < 2:
            digito2 = 0
        else:
            digito2 = 11 - resto

        # Verifica se os dígitos verificadores calculados coincidem com os dígitos do CNPJ
        if int(cnpj[12]) == digito1 and int(cnpj[13]) == digito2:
            return True
        else:
            return False


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

class MakeGenealogy:

    @staticmethod
    def tableToImageAnimal(pathDataBase:str, mainPath: str, codAnimal: str):
        #busca dados do animal:
        conn = sqlite3.connect(pathDataBase)
        cursor = conn.cursor()

        querySql = f'''SELECT codChip, nomeAnimal, nascimento, sexoAnimal FROM animais_data WHERE codChip="{codAnimal}"'''
        result = cursor.execute(querySql).fetchone()
        conn.close()
        print(result, " this is result")

        cell_text = [["MicroChip", result[0]],
                    ["Nome", result[1]], 
                    ["Nasc.:", result[2]],
                    ["Sexo", result[3]]]

        # Tamanho da imagem (largura x altura)
        largura = 300
        altura = 100

        # Crie uma figura com o tamanho especificado
        fig, ax = plt.subplots(figsize=(largura / 100, altura / 100))

        # Desenhe uma tabela

        table = ax.table(cellText=cell_text, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])

        # Estilize a tabela com bordas em negrito
        for (i, j), cell in table._cells.items():
            if i == 0:
                cell.set_text_props(weight='bold')
            cell.set_linewidth(2)
            cell.set_fontsize(12)

        # Remova os eixos e salve a imagem como um arquivo PNG
        ax.axis('off')
        plt.savefig(mainPath+'\\tabelaAnimal.png', bbox_inches='tight', pad_inches=0, format='png', dpi=300)

    @staticmethod
    def tableToImageRelativies(pathDataBase:str, mainPath: str, parentesco: str,  codAnimal: str):
        #busca dados do animal:
        conn = sqlite3.connect(pathDataBase)
        cursor = conn.cursor()

        querySql = f'''SELECT codChip, nomeAnimal FROM animais_data WHERE codChip="{codAnimal}"'''
        print(querySql)
        result = cursor.execute(querySql).fetchone()
        print(result, " this is result")

        cell_text = [["MicroChip", result[0]],
                    ["Nome", result[1]]]

        # Tamanho da imagem (largura x altura)
        largura = 300
        altura = 100

        # Crie uma figura com o tamanho especificado
        fig, ax = plt.subplots(figsize=(largura / 100, altura / 100))

        # Desenhe uma tabela

        table = ax.table(cellText=cell_text, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])

        # Estilize a tabela com bordas em negrito
        for (i, j), cell in table._cells.items():
            if i == 0:
                cell.set_text_props(weight='bold')
            cell.set_linewidth(2)
            cell.set_fontsize(12)

        # Remova os eixos e salve a imagem como um arquivo PNG
        ax.axis('off')
        plt.savefig(mainPath+f'\\tabelaAnimal{parentesco}.png', bbox_inches='tight', pad_inches=0, format='png', dpi=300)


    @staticmethod
    def getAllRelativies(pathDataBase:str, codChip: str):
        connection = sqlite3.connect(pathDataBase)
        cursor = connection.cursor()

        listaCods = [codChip]
        buscaPaiEMae = f'''SELECT codChipPai, codChipMae FROM animais_data WHERE codChip = "{listaCods[0]}" '''
        resultBuscaPaiEMae = cursor.execute(buscaPaiEMae).fetchone()
        print(resultBuscaPaiEMae)

        if resultBuscaPaiEMae:
            listaCods.append(resultBuscaPaiEMae[0])
            listaCods.append(resultBuscaPaiEMae[1])

        for i in range(1, 7):
            buscaPaiEMae = f'''SELECT codChipPai, codChipMae FROM animais_data WHERE codChip = "{listaCods[i]}"'''
            resultBuscaPaiEMae = cursor.execute(buscaPaiEMae).fetchone()
            listaCods.append(resultBuscaPaiEMae[0])
            listaCods.append(resultBuscaPaiEMae[1])
            print(resultBuscaPaiEMae)

        connection.close()

        genealogia = [
            "Animal", "Pai", "Mãe", 
            "Avô Paterno","Avó Paterno","Avô Materna", "Avó Materna",
            "Bisavô1","Bisavó1","Bisavô2","Bisavó2", "Bisavô3","Bisavó3", "Bisavô3","Bisavó3"]
        
        listaGeral = []
        for i in range(0, 15):
            listaGeral.append([genealogia[i], listaCods[i]] )
        return listaGeral
    
    @staticmethod
    def createGenealogyImage(mainPath: str):

        #img = mpimg.imread('table_images/table1.png')
        G = nx.Graph()
        G.add_node(0, image=mpimg.imread(mainPath +'\\tabelaAnimal.png'), layer="camada1")
        G.add_node(1, image=mpimg.imread(mainPath +'\\tabelaAnimalPai.png'), layer="camada2")
        G.add_node(2, image=mpimg.imread(mainPath +'\\tabelaAnimalMãe.png'), layer="camada2")
        G.add_node(3, image=mpimg.imread(mainPath +'\\tabelaAnimalAvô Paterno.png'), layer="camada3")
        G.add_node(4, image=mpimg.imread(mainPath +'\\tabelaAnimalAvó Paterno.png'), layer="camada3")
        G.add_node(5, image=mpimg.imread(mainPath +'\\tabelaAnimalAvô Materna.png'), layer="camada3")
        G.add_node(6, image=mpimg.imread(mainPath +'\\tabelaAnimalAvô Materna.png'), layer="camada3")
        G.add_node(7, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavô.png'), layer="camada4")
        G.add_node(8, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavó.png'), layer="camada4")
        G.add_node(9, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavô1.png'), layer="camada4")
        G.add_node(10, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavó1.png'), layer="camada4")
        G.add_node(11, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavô2.png'), layer="camada4")
        G.add_node(12, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavó2.png'), layer="camada4")
        G.add_node(13, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavô3.png'), layer="camada4")
        G.add_node(14, image=mpimg.imread(mainPath +'\\tabelaAnimalBisavó3.png'), layer="camada4")

        print(G.nodes())
        G.add_edge(0, 1, layer='camada1-2')
        G.add_edge(0, 2, layer='camada1-2')

        G.add_edge(1, 3, layer='camada2-3')
        G.add_edge(1, 4, layer='camada2-3')
        G.add_edge(2, 5, layer='camada2-3')
        G.add_edge(2, 6, layer='camada2-3')

        G.add_edge(3, 7, layer='camada3-4')
        G.add_edge(3, 8, layer='camada3-4')
        G.add_edge(4, 9, layer='camada3-4')
        G.add_edge(4, 10, layer='camada3-4')
        G.add_edge(5, 11, layer='camada3-4')
        G.add_edge(5, 12, layer='camada3-4')
        G.add_edge(6, 13, layer='camada3-4')
        G.add_edge(2, 14, layer='camada3-4')

        # Use o layout multipartite
        pos = nx.multipartite_layout(G, subset_key="layer")

        #fig = plt.figure(figsize=(10, 10))

        width, height = 11.7, 8.3  # 297mm x 210mm
        # Resolução em DPI desejada (por exemplo, 300 DPI para impressão de alta qualidade)
        dpi = 300
        # Calcule o número de pixels necessário para atingir a resolução desejada
        pixel_width = int(width * dpi)
        pixel_height = int(height * dpi)
        fig = plt.figure(figsize=(pixel_width / dpi, pixel_height / dpi), dpi=dpi)

        ax = plt.subplot()
        ax.set_aspect('equal')
        nx.draw_networkx_edges(G, pos, ax=ax, width=2.0)

        # Remova as linhas abaixo que definem limites
        # plt.xlim(-1.5, 1.5)
        # plt.ylim(-1.5, 1.5)

        # Restante do código
        trans = ax.transData.transform
        trans2 = fig.transFigure.inverted().transform

        piesize = 0.1  # this is the image size
        p2 = piesize / 2.0
        for n in G:
            xx, yy = trans(pos[n])  # figure coordinates
            xa, ya = trans2((xx, yy))  # axes coordinates
            a = plt.axes([xa - p2, ya - p2, piesize, piesize])
            a.set_aspect('equal')
            a.imshow(G._node[n]['image'])
            a.axis('off')
        ax.axis('off')

        plt.savefig(mainPath+"\\graph_image.png", bbox_inches="tight", pad_inches=0)