sal = float(input('Salario bruto: '))
ini = sal * 0.10
print('salario previdencia: ', {ini})
imp = sal * 0.05
print('salario de imposto', {imp})
inir = sal - ini
impr = inir - imp
resto = impr
print(resto)