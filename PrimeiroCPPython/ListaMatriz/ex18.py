# Calcular a média de uma matriz:

def media_matriz(mat):
    total = 0
    contagem = 0
    for linha in mat:
        total += sum(linha)
        contagem += len(linha)
    media = total / contagem if contagem > 0 else 0
    return media

# Exemplo de uso:
matriz_exemplo = [
    [5, 8, 1],
    [3, 9, 2],
    [7, 4, 6]
]
print(media_matriz(matriz_exemplo))  # Saída: média dos elementos da matriz
