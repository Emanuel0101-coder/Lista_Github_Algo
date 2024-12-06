import math

a = float(input('info o valor 01: '))
if a == 0:
    print('não é equação de segundo grau')
else:
    b = float(input('info o valor 02: '))
    c = float(input('info o valor 03: '))
 
    # Calcula o delta
    delta = a**2 + b +c
    
    # Verifica o valor do delta
    if delta < 0:
        print("A equação não possui raízes reais.")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(f"A equação possui uma única raiz real: {raiz}")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"A equação possui duas raízes reais: {raiz1} e {raiz2}")

