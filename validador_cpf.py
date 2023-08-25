peso = [10,9,8,7,6,5,4,3,2]
cpf = []

print('Informe os nove primeiros digitos do cpf: ')
for i in range(1, 10):
    try:
        digito = int(input())
        if digito < 0:
            print('Digite apenas um numero maior ou igual a zero!')
        else:
            cpf.append(digito)
    except ValueError:
        print('Digite um valor numérico válido!')

print(cpf) 

n = 3.14159
raio = float(input())
area = n*(raio**2)
print(f"A= {area:.4f}")
print()