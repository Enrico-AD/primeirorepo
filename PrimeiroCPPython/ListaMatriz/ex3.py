import random

def cria_matriz_5x7():
    matriz = [[random.randint(0, 1000) for _ in range(7)] for _ in range(5)]
    return matriz

# Exemplo de impressão da matriz:
for linha in cria_matriz_5x7():
    print(linha)
