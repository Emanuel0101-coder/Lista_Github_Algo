"""
Faça um programa que leia um vetor com N elementos formado por valores do tipo inteiro. Crie então dois novos vetores, 
um com os valores pares e outro com os valores ímpares do vetor original.
"""

V = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
V2 = []
V3 = []
total = len(V)

for c in V:
    if c % 2 == 0:              #vai verificar se o valor que está em V é divisivel por 2, se for é par, se não é impar
        V2.append(c)
    else:
        V3.append(c)

print(V)
print(V2)
print(V3)
