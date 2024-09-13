import random

def cria_matriz_30x50():
    matriz = [[random.randint(1, 200) for _ in range(50)] for _ in range(30)]
    return matriz

def conta_elementos(matriz):
    conta = [0] * 201  # Cria uma lista de contagem com 201 posições (0 a 200)
    for linha in matriz:
        for num in linha:
            conta[num] += 1
    return conta

# Exemplo:
matriz = cria_matriz_30x50()
contagem = conta_elementos(matriz)
print(contagem)  # Exibe a contagem de cada número entre 1 e 200
