def esta_ordenada(lista):
    # Itera pela lista comparando cada elemento com o próximo
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False  # Retorna False se encontrar um elemento fora de ordem
    return True  # Retorna True se a lista estiver ordenada

# Testando
lista = [1.1, 2.2, 3.3, 4.4, 5.5]
print(esta_ordenada(lista))  # Esperado: True
lista_desordenada = [5.5, 3.3, 4.4, 2.2, 1.1]
print(esta_ordenada(lista_desordenada))  # Esperado: False
