n1 = float(input('Digite o valor numero 1: '))
n2 = float(input('Digite o valor numero 2: '))
opo = str(input('Digite as Operações: (+) soma, (-) subtração, (/) divisão, (*) multiplicação'))

if opo == '+':
    n3 = n1+n2 
    print(n3)
elif opo == '-':
    n3 = n1-n2
    print(n3)
elif opo == '/':
    n3 = n1/n2
    print(n3)
elif opo == '*':
    n3 = n1*n2
    print(n3)