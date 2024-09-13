def imprime_jogo_da_velha():
    matriz = [['x', 'o', 'x'],
              ['o', 'x', ' '],
              ['o', 'x', ' ']]
    for linha in matriz:
        print(' '.join(linha))

imprime_jogo_da_velha()
