frase = 'O Python é uma linguagem de programação multiparadima'

i = 0
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_letra_apareceu = frase.count(letra_atual)
    print(letra_atual, quantas_vezes_letra_apareceu)
    i += 1


