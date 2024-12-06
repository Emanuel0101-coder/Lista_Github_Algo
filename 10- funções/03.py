def conc(F):
    C = (F -32) * 5 /9
    return C
def conf(C):
    F = (C * 9 /5) +32
    return F

F = float(input('digite a temperatura em ºF: '))
C = float(input('digite a temperatura em ºC: '))

print(f'{F}ºF em Celsius é: {conc(F)}ºC')
print(f'{C}ºC em Fahrenheit é: {conf(C)}ºF')