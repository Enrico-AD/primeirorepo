# Algoritmo de busca simples
def busca_simples(vetor, valor):
    # Itera sobre todos os elementos do vetor
    for i in range(len(vetor)):
        # Verifica se o valor procurado está na posição atual
        if vetor[i] == valor:
            return i  # Retorna a posição se encontrado
    return -1  # Retorna -1 se não for encontrado

# Algoritmo de busca binária
def busca_binaria(vetor, valor):
    # Define os limites de busca
    inicio = 0
    fim = len(vetor) - 1

    while inicio <= fim:
        # Calcula o meio do vetor
        meio = (inicio + fim) // 2

        # Verifica se o valor está no meio
        if vetor[meio] == valor:
            return meio
        # Se o valor for menor, move o fim para a esquerda
        elif vetor[meio] > valor:
            fim = meio - 1
        # Se o valor for maior, move o início para a direita
        else:
            inicio = meio + 1

    return -1  # Retorna -1 se não for encontrado

# Testando busca simples e binária
vetor = [1, 3, 5, 7, 9]
valor = 4
print(f"Busca simples: {busca_simples(vetor, valor)}")  # Não encontrado, retorna -1
print(f"Busca binária: {busca_binaria(vetor, valor)}")  # Não encontrado, retorna -1
