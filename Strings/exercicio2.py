"""
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
"""

nome = str(input('digite o nome: '))
#cont e space, para axuiliar na contagem de vogais e nos espaços em branco
cont = 0
space = 0
con = nome.lower()
#nesse loop, vai percorrer o len(con) que já foi colocado tudo em minusculo, irá ver se possui vogal e espaço em branco
#com os if's  
for i in range(len(con)):
    if con[i] == 'a' or con[i] == 'e' or con[i] == 'i' or con[i] == 'o' or con[i] == 'u':
        cont += 1
    if con[i] == ' ':
        space += 1
print(cont)  
print(space)  