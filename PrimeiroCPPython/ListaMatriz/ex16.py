def negativo_imagem(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    for i in range(linhas):
        for j in range(colunas):
            mat[i][j] = 255 - mat[i][j]
    return mat

# Exemplo:
imagem_cinza_exemplo = [[100, 150], [200, 50]]
print(negativo_imagem(imagem_cinza_exemplo))  # Aplica o negativo da imagem
