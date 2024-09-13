def coluna_com_maior_valor(mat):
    ultima_linha = mat[-1]
    maior_valor = max(ultima_linha)
    indice_maior = ultima_linha.index(maior_valor)
    return indice_maior

# Exemplo:
matriz_exemplo = [
    [100.23, 200.94, 240.21],
    [210.53, 302.32, 280.51],
    [420.67, 720.94, 430.09],
    [731.43, 1224.20, 950.81]  # Totais por coluna
]
print(coluna_com_maior_valor(matriz_exemplo))  # Saída: índice da coluna com maior total
