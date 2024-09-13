# Função de busca simples dos slides
def busca_simples_slide(vetor, valor):
    for i in range(len(vetor)):
        if vetor[i] == valor:
            return i
    return -1

# Função de busca binária dos slides
def busca_binaria_slide(vetor, valor):
    inicio = 0
    fim = len(vetor) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if vetor[meio] == valor:
            return meio
        elif vetor[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

# Testando
vetor = [10, 20, 30, 40, 50]
print(busca_simples_slide(vetor, 30))  # Esperado: 2
print(busca_binaria_slide(vetor, 30))  # Esperado: 2
