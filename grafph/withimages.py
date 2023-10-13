import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import networkx as nx

img = mpimg.imread('table_images/table1.png')
G = nx.Graph()
G.add_node(0, image=mpimg.imread('table_images/aqui.png'), layer="camada1")
G.add_node(1, image=mpimg.imread('table_images/table2.png'), layer="camada2")
G.add_node(2, image=mpimg.imread('table_images/table3.png'), layer="camada2")
G.add_node(3, image=mpimg.imread('table_images/table4.png'), layer="camada3")
G.add_node(4, image=mpimg.imread('table_images/table5.png'), layer="camada3")
G.add_node(5, image=mpimg.imread('table_images/table6.png'), layer="camada3")
G.add_node(6, image=mpimg.imread('table_images/table7.png'), layer="camada3")

print(G.nodes())
G.add_edge(0, 1, layer='camada1-2')
G.add_edge(0, 2, layer='camada1-2')
G.add_edge(1, 3, layer='camada2-3')
G.add_edge(1, 4, layer='camada2-3')
G.add_edge(2, 5, layer='camada2-3')
G.add_edge(2, 6, layer='camada2-3')

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

ax = plt.subplot(111)
ax.set_aspect('equal')
nx.draw_networkx_edges(G, pos, ax=ax)

# Remova as linhas abaixo que definem limites
# plt.xlim(-1.5, 1.5)
# plt.ylim(-1.5, 1.5)

# Restante do código
trans = ax.transData.transform
trans2 = fig.transFigure.inverted().transform

piesize = 0.1   # this is the image size
p2 = piesize / 2.0
for n in G:
    xx, yy = trans(pos[n])  # figure coordinates
    xa, ya = trans2((xx, yy))  # axes coordinates
    a = plt.axes([xa - p2, ya - p2, piesize, piesize])
    a.set_aspect('equal')
    a.imshow(G._node[n]['image'])
    a.axis('off')
ax.axis('off')

plt.savefig("graph_image.png", bbox_inches="tight", pad_inches=0)
plt.show()


