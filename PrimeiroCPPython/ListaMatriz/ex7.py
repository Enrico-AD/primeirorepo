def substituir_matriz(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] <= 127:
                mat[i][j] = 0
            else:
                mat[i][j] = 255
    return mat

# Exemplo:
matriz_exemplo = [[100, 200], [128, 127]]
print(substituir_matriz(matriz_exemplo))  # Saída: [[0, 255], [255, 0]]
