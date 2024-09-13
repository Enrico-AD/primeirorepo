# Função que multiplica duas matrizes:

def multiplica_matrizes(a, b):
    linhas_a = len(a)
    colunas_a = len(a[0])
    colunas_b = len(b[0])

    # Cria a matriz resultado com zeros
    resultado = [[0] * colunas_b for _ in range(linhas_a)]

    # Multiplica matrizes
    for i in range(linhas_a):
        for j in range(colunas_b):
            for k in range(colunas_a):
                resultado[i][j] += a[i][k] * b[k][j]
    return resultado


# Exemplo de uso:
a_exemplo = [
    [1, 2],
    [3, 4],
    [5, 6]
]
b_exemplo = [
    [7, 8, 9],
    [10, 11, 12]
]
resultado = multiplica_matrizes(a_exemplo, b_exemplo)
print(resultado)  # Saída: matriz resultado da multiplicação
