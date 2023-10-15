import matplotlib.pyplot as plt

# Tamanho da imagem (largura x altura)
largura = 300
altura = 100

# Crie uma figura com o tamanho especificado
fig, ax = plt.subplots(figsize=(largura / 100, altura / 100))

# Desenhe uma tabela
cell_text = [['Microchip', '001010100101'],
             ['Nome', 'Coelho'],
             ['Nasc', '12/04/1993']]

table = ax.table(cellText=cell_text, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])

# Estilize a tabela com bordas em negrito
for (i, j), cell in table._cells.items():
    if i == 0:
        cell.set_text_props(weight='bold')
    cell.set_linewidth(2)
    cell.set_fontsize(12)

# Remova os eixos e salve a imagem como um arquivo PNG
ax.axis('off')
plt.savefig('tabela.png', bbox_inches='tight', pad_inches=0, format='png', dpi=100)

# Exiba a imagem (opcional)
plt.show()
