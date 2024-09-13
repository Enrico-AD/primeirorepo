def bubble_sort_decrescente(lista):
    n = len(lista)
    # Laço para passar por todos os elementos da lista
    for i in range(n):
        for j in range(0, n-i-1):
            # Troca os elementos se o anterior for menor que o próximo (ordem decrescente)
            if lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando
lista = [64, 34, 25, 12, 22, 11, 90, 5, 45, 67, 2, 18, 23, 85, 3]
bubble_sort_decrescente(lista)
print(lista)  # Lista em ordem decrescente: [90, 85, 67, 64, 45, 34, 25, 23, 22, 18, 12, 11, 5, 3, 2]
