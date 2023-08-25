nome = input('Digite seu nome:')
while True:
    try:
        idade = int(input('Digite sua idade:'))
    except ValueError:
        print('Entrada inválida! Digite apenas números inteiros.')

print(f'Seu nome é {nome}')
print()