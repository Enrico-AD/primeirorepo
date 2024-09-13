def totais_por_linha(mat):
    for linha in mat:
        total = sum(linha[:-1])  # Soma todos os elementos, exceto o último
        linha[-1] = total  # Coloca o total na última coluna
    return mat

# Exemplo:
matriz_exemplo = [
    [100.23, 200.94, 240.21, 110.38, 500.29, 300.00, 0],
    [210.53, 302.32, 280.51, 500.22, 750.45, 233.01, 0],
    [420.67, 720.94, 430.09, 1410.87, 567.92, 373.43, 0]
]
print(totais_por_linha(matriz_exemplo))  # Atualiza a última coluna com os totais
