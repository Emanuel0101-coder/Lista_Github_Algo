"""
Ao observar a sequência de números abaixo, descubra qual das opções completa a série.

66, 59, 52, 45, 38, ??

32
35
31
41
43
"""

#Resposta: 31, visto que segue um padrão interessante, ele dimini 7 vezes cada passada

vet = [66, 59, 52, 45, 38]

for c in vet:
    sequencia = c - 7
    print(sequencia)

