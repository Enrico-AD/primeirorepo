def somaPos(matriz):
    soma = 0
    for linha in matriz:
        for num in linha:
            if num > 0:
                soma += num
    return soma

# Exemplo:
matriz_exemplo = [[-1, 2, 3], [-4, 5, -6]]
print(somaPos(matriz_exemplo))  # Saída: 10
