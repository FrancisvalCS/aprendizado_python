nome = input('Digite seu nome:')
find = input('Digite o que deseja encontrar: ')

if find in nome:
    print(f'{find} está em {nome}')
else:
    print(f'{find} não está em {nome}')



