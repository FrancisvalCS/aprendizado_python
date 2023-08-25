try:
    num = int(input('Digite um número:'))
    if num % 2 == 0:
        print("Numero par")
    else:
        print("Numero ímpar")
except ValueError:
    print("Não é um número inteiro")