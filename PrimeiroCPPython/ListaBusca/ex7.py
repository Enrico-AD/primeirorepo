def busca_simples_ocorrencias(lista, x):
    # Lista para armazenar as posições encontradas
    ocorrencias = []
    for i in range(len(lista)):
        if lista[i] == x:
            ocorrencias.append(i)
    return ocorrencias if ocorrencias else -1

# Testando
lista = [1, 2, 3, 2, 4, 2]
x = 2
print(busca_simples_ocorrencias(lista, x))  # Esperado: [1, 3, 5]
