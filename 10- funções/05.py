n1 = float(input('Digite o valor n1: '))
n2 = float(input('Digite o valor n2: '))
n3 = float(input('Digite o valor n3: '))
def tri(n1,n2,n3):
    if (n1 + n2 < n3) or (n2 + n3 < n1):
        return ('não é um triangulo')
    elif (n1 == n2 or n1 == n3 or n3 == n2) and (n1 != n2 or n1 != n3 or n2 != n3):
        return ('isósceles')
    elif (n1 != n2 and n1 != n3 and n2 != n3):
        return ('escaleno')
    elif (n1 == n2 and n1 == n3 and n2 == n3):
        return ('equilátero')
print(tri(n1,n2,n3))