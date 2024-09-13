def converte_para_cinza(red, green, blue):
    linhas = len(red)
    colunas = len(red[0])
    gray = [[0] * colunas for _ in range(linhas)]  # Matriz vazia para imagem em tons de cinza
    for i in range(linhas):
        for j in range(colunas):
            gray[i][j] = int(0.30 * red[i][j] + 0.59 * green[i][j] + 0.11 * blue[i][j])
    return gray

# Exemplo de como usar:
# Suponha que red, green, blue sejam matrizes RGB extraídas de uma imagem
# gray_image = converte_para_cinza(red, green, blue)
