import random

def rearranjar_lista(v):
    # Escolhe uma posição aleatória p
    p = random.randint(0, len(v) - 1)
    elemento_p = v[p]
    menores = [x for x in v if x < elemento_p]  # Todos os elementos menores que v[p]
    maiores_iguais = [x for x in v if x >= elemento_p]  # Todos os elementos maiores ou iguais a v[p]
    rearranjada = menores + maiores_iguais  # Combina as duas listas
    return rearranjada, p

# Testando
v = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
rearranjada, p = rearranjar_lista(v)
print(f"Lista rearranjada: {rearranjada}")
print(f"Posição p: {p}")
