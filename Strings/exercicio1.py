"""
Faça um programa que permita ao usuário digitar o seu nome e em seguida imprima o nome do usuário de trás para frente 
utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar 
letras maiúsculas ou minúsculas.
"""

n = input('Digite o seu nome: ')
n1 = ''
for i in range(len(n) - 1, -1, -1):         #vai inverter nome
    n1 += n[i]
n1 = n1.upper()  
print(n1)