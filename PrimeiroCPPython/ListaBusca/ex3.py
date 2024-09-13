def eliminar_repetidos(lista):
    # Cria uma nova lista para armazenar elementos únicos
    nova_lista = []
    for elemento in lista:
        # Verifica se o elemento já não está na nova lista
        if elemento not in nova_lista:
            nova_lista.append(elemento)
    return nova_lista

# Testando
lista = [1, 2, 2, 3, 4, 4, 5]
print(eliminar_repetidos(lista))  # Esperado: [1, 2, 3, 4, 5]
