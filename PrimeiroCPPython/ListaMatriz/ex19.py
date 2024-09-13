# Função que calcula a soma de todos os elementos de uma matriz:

def soma_matriz(mat):
    soma = 0
    for linha in mat:
        soma += sum(linha)
    return soma

# Exemplo de uso:
matriz_exemplo = [
    [5, 8, 1],
    [3, 9, 2],
    [7, 4, 6]
]
print(soma_matriz(matriz_exemplo))  # Saída: soma dos elementos da matriz
