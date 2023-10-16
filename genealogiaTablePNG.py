#gerar primeira tabela

import matplotlib.pyplot as plt
import sqlite3 
import os
from Controller import *

mainDir = os.path.dirname(os.path.abspath(__file__))
pathDataBase = mainDir+ "\Resources\DataBase\main.db"
#busca dados do animal:
conn = sqlite3.connect(pathDataBase)
cursor = conn.cursor()

codAnimal = 28
querySql = f'''SELECT codChip, nomeAnimal, nascimento, sexoAnimal FROM animais_data WHERE codChip="{codAnimal}"'''
result = cursor.execute(querySql).fetchone()

cell_text = [["MicroChip", result[0]],
             ["Nome", result[1]],
             ["Nascimento", result[2]],
             ["sexoAnimal", result[3]]]

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
plt.savefig('tabelaAnimal.png', bbox_inches='tight', pad_inches=0, format='png', dpi=300)

# Exiba a imagem (opcional)

#gerar tabela dos demais pertencentes a genealogia(somente chip e tipo sanquineo ? )

import matplotlib.pyplot as plt
import sqlite3 
import os

mainDir = os.path.dirname(os.path.abspath(__file__))
pathDataBase = mainDir+ "\Resources\DataBase\main.db"
#busca dados do animal:
conn = sqlite3.connect(pathDataBase)
cursor = conn.cursor()

codAnimal = 28
querySql = f'''SELECT codChip, nomeAnimal, nascimento, sexoAnimal FROM animais_data WHERE codChip="{codAnimal}"'''
result = cursor.execute(querySql).fetchone()

cell_text = [["MicroChip", result[0]],
             ["Nome", result[1]],
             ["Nascimento", result[2]],
             ["sexoAnimal", result[3]]]

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
plt.savefig('tabelaAnimal.png', bbox_inches='tight', pad_inches=0, format='png', dpi=300)

