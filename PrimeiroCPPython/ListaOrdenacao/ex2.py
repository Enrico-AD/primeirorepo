def bubble_sort(lista):
    n = len(lista)
    # Laço para passar por todos os elementos da lista
    for i in range(n):
        for j in range(0, n-i-1):
            # Troca os elementos se estiverem fora de ordem
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando com uma lista de 15 elementos
lista = [64, 34, 25, 12, 22, 11, 90, 5, 45, 67, 2, 18, 23, 85, 3]
bubble_sort(lista)
print(lista)  # Lista ordenada: [2, 3, 5, 11, 12, 18, 22, 23, 25, 34, 45, 64, 67, 85, 90]
