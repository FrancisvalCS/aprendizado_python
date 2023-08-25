usuario = [] #lista vazia


usr = input('Digite um valor a ser adicionado na lista: ')
while usr != 'fim':
    usuario.append(usr)
    usr = input('Digite um valor a ser adicionado na lista: ')
print(usuario)
