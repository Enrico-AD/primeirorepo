def soma_dois_binaria(lista, x):
    # Ordena a lista
    lista.sort()

    # Utiliza dois ponteiros para procurar a soma
    inicio = 0
    fim = len(lista) - 1

    while inicio < fim:
        soma = lista[inicio] + lista[fim]
        if soma == x:
            return lista[inicio], lista[fim]
        elif soma < x:
            inicio += 1
        else:
            fim -= 1
    return None

# Testando
lista = [2, 5, -7, 9, 3, 10, 15, 6]
x = 11
print(soma_dois_binaria(lista, x))  # Esperado: (2, 9) ou (5, 6)
