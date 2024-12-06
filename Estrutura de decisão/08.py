a = float(input('informe o tamanho de um triangulo: '))
b = float(input('informe o tamanho de um triangulo: '))
c = float(input('informe o tamanho de um triangulo: '))

sum1 = a+b
sum2 = b+c
sum3 = c+a

if a <= sum2 and b <= sum3 and c <= sum1:
    print('isso é um triangulo')
    if (a == b or a == c or b == c) and (c != a or b != a or c != b):
        print('isso é um triangulo isósceles')
    elif a != b and a != c and c != b:
        print('isso é um triangulo escaleno')
    elif a == b and b == a and c == a:
        print('isso é um triangulo equilátero')
else:
    print('isso não é um triangulo')