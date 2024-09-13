def soma_dois_elementos(lista, x):
    # Percorre a lista comparando cada elemento com os demais
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            # Verifica se a soma dos dois elementos é igual a x
            if lista[i] + lista[j] == x:
                return lista[i], lista[j]
    return None

# Testando
lista = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11
print(soma_dois_elementos(lista, x))  # Esperado: (2, 9) ou (5, 6)
