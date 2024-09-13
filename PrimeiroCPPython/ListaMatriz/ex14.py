def rotaciona_180(mat):
    return [linha[::-1] for linha in mat[::-1]]  # Inverte linhas e colunas

# Exemplo:
imagem_exemplo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotaciona_180(imagem_exemplo))  # Saída: imagem rotacionada 180 graus
