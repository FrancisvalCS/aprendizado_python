cred = []

print('O que deseja fazer?')
print('1-Cadastrar nova credencial')
print('2-Realizar acesso')

try:
    vl = int(input('Informe a sua opção: '))
    while vl != 0:
        if vl >= 1 & vl <= 2:
            if vl == 1:
                ncred = input('Informe a nova credencial: ')
                cred.append(ncred)
            else:
                credencial = input('Digite a sua credencial: ')
                if credencial in cred:
                    print('Seja bem vindo, você realizou o acesso.')
                else:
                    print('Acesso negado!')
        vl = int(input('Informe a sua opção: '))
except ValueError:
    print('Não há um valor correspondente no menu!')