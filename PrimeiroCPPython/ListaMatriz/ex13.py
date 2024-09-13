def espelha_vertical(mat):
    linhas = len(mat)
    colunas = len(mat[0])
    for i in range(linhas):
        for j in range(colunas // 2):
            mat[i][j], mat[i][colunas - 1 - j] = mat[i][colunas - 1 - j], mat[i][j]
    return mat

# Exemplo:
imagem_exemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(espelha_vertical(imagem_exemplo))  # Saída: matriz espelhada verticalmente
