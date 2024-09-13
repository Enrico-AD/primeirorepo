def soma(matriz):
    soma_positivos = 0
    soma_negativos = 0
    for linha in matriz:
        for num in linha:
            if num > 0:
                soma_positivos += num
            elif num < 0:
                soma_negativos += num
    return (soma_positivos, soma_negativos)

# Exemplo:
matriz_exemplo = [[-1, 2, 3], [-4, 5, -6]]
print(soma(matriz_exemplo))  # Saída: (10, -11)
