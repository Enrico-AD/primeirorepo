def bubble_sort_strings(lista):
    n = len(lista)
    # Laço para passar por todos os elementos da lista
    for i in range(n):
        for j in range(0, n-i-1):
            # Troca os elementos se o anterior for maior que o próximo (ordem alfabética)
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando com lista de strings
lista_strings = ["banana", "maçã", "laranja", "uva", "kiwi"]
bubble_sort_strings(lista_strings)
print(lista_strings)  # Esperado: ['banana', 'kiwi', 'laranja', 'maçã', 'uva']
