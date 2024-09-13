def bubble_sort_simples(lista):
    n = len(lista)
    # Laços de repetição encadeados
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando
lista = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_simples(lista)
print(lista)  # Esperado: [11, 12, 22, 25, 34, 64, 90]
