def busca_binaria_ocorrencias(lista, x):
    inicio = 0
    fim = len(lista) - 1
    ocorrencias = []

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == x:
            # Busca para esquerda e direita do elemento encontrado
            ocorrencias.append(meio)
            esquerda = meio - 1
            direita = meio + 1
            while esquerda >= 0 and lista[esquerda] == x:
                ocorrencias.append(esquerda)
                esquerda -= 1
            while direita < len(lista) and lista[direita] == x:
                ocorrencias.append(direita)
                direita += 1
            return sorted(ocorrencias)
        elif lista[meio] < x:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Testando
lista = [1, 2, 2, 2, 3, 4, 5]
x = 2
print(busca_binaria_ocorrencias(lista, x))  # Esperado: [1, 2, 3]
