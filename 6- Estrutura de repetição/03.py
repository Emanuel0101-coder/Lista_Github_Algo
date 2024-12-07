'''Faça um programa que peça dois números, base e expoente, 
calcule e imprima o primeiro número elevado ao segundo número.
Não utilize a função de potência da linguagem.'''
x = int(input('Digite o base: '))
z = int(input('Digite o expoente: '))
total = 1
for i in range (z):
    total *= x
print(total)