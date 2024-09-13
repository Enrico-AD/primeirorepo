def ordenar_tuplas(lista):
    # Laço externo para ordenar a lista pelo nome e idade
    for i in range(len(lista)):
        for j in range(0, len(lista) - i - 1):
            # Primeiro compara o nome
            if lista[j][0] > lista[j + 1][0]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            # Se os nomes forem iguais, compara a idade
            elif lista[j][0] == lista[j + 1][0] and lista[j][1] > lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Testando
lista_tuplas = [("Joao", 25), ("Ana", 30), ("Carlos", 22), ("Ana", 18)]
ordenar_tuplas(lista_tuplas)
print(lista_tuplas)  # Esperado: [('Ana', 18), ('Ana', 30), ('Carlos', 22), ('Joao', 25)]
