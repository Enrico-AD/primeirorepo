def getDimensao(mat):
    linhas = len(mat)
    colunas = len(mat[0]) if linhas > 0 else 0
    return (linhas, colunas)

# Exemplo:
matriz_exemplo = [[1, 2, 3], [4, 5, 6]]
print(getDimensao(matriz_exemplo))  # Saída: (2, 3)
