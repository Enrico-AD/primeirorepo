def totais_por_coluna(mat):
    colunas = len(mat[0])
    total_coluna = [0] * colunas
    for i in range(len(mat) - 1):  # Exceto a última linha
        for j in range(colunas):
            total_coluna[j] += mat[i][j]
    mat[-1] = total_coluna  # Preenche a última linha com os totais das colunas
    return mat

# Exemplo:
matriz_exemplo = [
    [100.23, 200.94, 240.21],
    [210.53, 302.32, 280.51],
    [420.67, 720.94, 430.09],
    [0, 0, 0]  # Última linha inicialmente vazia
]
print(totais_por_coluna(matriz_exemplo))  # Preenche a última linha com os totais
