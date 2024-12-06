"""
Faça um programa para ler dois vetores V1 e V2 de 15 números cada. Calcular e imprimir a quantidade de vezes que V1 e V2 
possuem os mesmos números e nas mesmas posições.
"""

V1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58, 29, 90, 97, 178]
V2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 58, 64, 43, 88, 203]
cont = 0

for c in range(15):
    if V1[c] == V2[c]:
        cont += 1
print('É igual até a posição {}'.format(cont))
