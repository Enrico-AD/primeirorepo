def busca(mat, x):
    for i, linha in enumerate(mat):
        if x in linha:
            return [i, linha.index(x)]
    return [-1, -1]

# Exemplo:
matriz_exemplo = [[1, 2, 3],
                  [4, 5, 6]]
print(busca(matriz_exemplo, 2))  # Saída


def busca(valor: object, matriz: list) -> list:

    lin = len(matriz)
    col = len(matriz[0])

    for i in range(lin):
        for j in range(col):
            if matriz[i][j] == valor:
                return [i, j]
    return [-1, -1]


mat = [
    [1, 2, 3, 4, 5],
    [3, 5, 6, 8, 9],
    [11, 22, 55, 6]
]

resp = busca(5, mat)
print(resp) #Saída
