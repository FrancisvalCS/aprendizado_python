num = input('Vou dobrar o numero que você digitar:')
try:
    print('STR:', num)
    num_f=float(num)
    print('FLOAT:', num_f)
    print(f'O dobro de {num} é {num_f * 2:.2f}')
except:
    print('Isso não é um número')