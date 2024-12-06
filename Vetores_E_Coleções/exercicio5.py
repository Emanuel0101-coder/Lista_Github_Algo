"""
Faça um programa que defina dois vetores A = [2, 4, 7, 13, 14, 15, 16] e B = [1, 6, 7, 11, 13, 16, 18] e faça as seguintes 
operações de conjuntos:

A ⋃ B: União (todos os valores de ambos os vetores)
A ⋂ B: Intersecção (apenas valores que existam em ambos)
A − B: Diferença (apenas valores que não apareçam simultaneamente em ambos conjuntos)
"""

A = [2, 4, 7, 13, 14, 15, 16]
B = [1, 6, 7, 11, 13, 16, 18]
C = []
D = []

#uniao
uniao = []
for a in A:
    if a not in uniao:
        uniao.append(a)
for b in B:
    if b not in uniao:
        uniao.append(b)
print(uniao)

#intersecção
for a in A:
    if a in B:                  #verifica se o elemento A está em B
        C.append(a)
print(C)

#Diferença
for a in A:
    if a not in B:              #verifica se o elemento A não está em B
        D.append(a)
print(D)


