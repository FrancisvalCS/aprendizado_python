def multiplicar(*args):
    total = 0
    for numero in args:
        total *= numero
    return total

multiplicacao = multiplicar(1,2,3,4,5)
print(multiplicacao)

