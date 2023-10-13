import sqlite3 
import os
import random

codChipto100 = list(range(1,100))
mainDir = os.path.dirname(os.path.abspath(__file__))
connection = sqlite3.connect(mainDir+ "\Resources\DataBase\main.db")
cursor = connection.cursor()

genealogia = [
    "cod", "codPai", "codMae", 
    "codAvoPatertno","codAvohPaterno","codAvoMaterno", "codAvohMaterna",
    "codBisa1","codBisa2","codBisa3","codBisa4","codBisa5","codBisa6","codBisa7","codBisa1"]


listaCods = ['28']
listaNames = []
buscaPaiEMae = f'''SELECT codChipPai, codChipMae FROM animais_data WHERE codChip = "{listaCods[0]}" '''
buscaNome = f'''SELECT nomeAnimal FROM animais_data WHERE codChip="{listaCods[0]}" '''
resultBuscaPaiEMae = cursor.execute(buscaPaiEMae).fetchone()
#resultBuscaNome = cursor.execute(buscaNome).fetchone()
#listaNames.append(resultBuscaNome[0])

#busca pai e mae
if resultBuscaPaiEMae:
    listaCods.append(resultBuscaPaiEMae[0])
    listaCods.append(resultBuscaPaiEMae[1])
    #buscaNome = f'''SELECT nomeAnimal FROM animais_data WHERE codChip="{listaCods[1]}"'''
    #resultBuscaNome = cursor.execute(buscaNome).fetchone()
    #listaNames.append(resultBuscaNome[0])
    #buscaNome = f'''SELECT nomeAnimal FROM animais_data WHERE codChip="{listaCods[2]}"'''
    #resultBuscaNome = cursor.execute(buscaNome).fetchone()
    #listaNames.append(resultBuscaNome[0])


for i in range(1, 7):
    buscaPaiEMae = f'''SELECT codChipPai, codChipMae FROM animais_data WHERE codChip = "{listaCods[i]}"'''
    resultBuscaPaiEMae = cursor.execute(buscaPaiEMae).fetchone()
    listaCods.append(resultBuscaPaiEMae[0])
    listaCods.append(resultBuscaPaiEMae[1])

for i in range(0, 15):
    buscaNome = f'''SELECT nomeAnimal FROM animais_data WHERE codChip="{listaCods[i]}"'''
    resultBuscaNome = cursor.execute(buscaNome).fetchone()
    listaNames.append(resultBuscaNome[0])


my_dict = {key: value for key, value in zip(listaCods, listaNames)}
print(my_dict)

'''
for i in range(1, 4):

    buscaPaiEMae = fSELECT codChipMae, codChipPai FROM animais_data WHERE codChip = "{cod}"
    print(2**i)
'''

connection.close()