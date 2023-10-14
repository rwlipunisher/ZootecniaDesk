from PIL import Image

# Carregue as duas imagens que você deseja sobrepor
imagem_de_fundo = Image.open('marcadagua.png')
imagem_sobreposta = Image.open('graph_image.png')

# Verifique se as dimensões das imagens são compatíveis (opcional)
if imagem_de_fundo.size != imagem_sobreposta.size:
    raise ValueError("As dimensões das imagens não são compatíveis.")

# Sobreponha a imagem sobre a imagem de fundo
imagem_de_fundo.paste(imagem_sobreposta, (0, 0), imagem_sobreposta)

# Salve a imagem resultante
imagem_de_fundo.save('imagem_sobreposta.png')

# Exiba a imagem (opcional)
imagem_de_fundo.show()
