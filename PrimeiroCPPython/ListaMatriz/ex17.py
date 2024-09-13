# Função que faz a verificação do maior elemento de cada linha de uma matriz:

def maior_elemento_linha(mat):
    maiores = []
    for linha in mat:
        maior = max(linha)
        maiores.append(maior)
    return maiores

# Exemplo de uso:
matriz_exemplo = [
    [5, 8, 1],
    [3, 9, 2],
    [7, 4, 6]
]
print(maior_elemento_linha(matriz_exemplo))  # Saída: [8, 9, 7]
