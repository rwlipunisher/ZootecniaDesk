import matplotlib.pyplot as plt

# Define the data for the table
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'San Francisco'],
    ['Charlie', 22, 'Los Angeles'],
]

# Create a figure and axis
fig, ax = plt.subplots()

# Create the table
table = ax.table(cellText=data, loc='center', cellLoc='center')

# Customize the appearance of the table
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)

# Hide the axis
ax.axis('off')

# Display the plot
plt.show()

# Exiba a imagem do grafo
plt.savefig("tree_diagram.png", format="png")

# Exiba o arquivo de imagem usando um visualizador de imagem externo (por exemplo, o programa padrão para exibir imagens)
import os
os.startfile("tree_diagram.png")