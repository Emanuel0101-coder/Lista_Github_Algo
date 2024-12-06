"""
Faça um programa que peça ao usuário duas strings diferentes, 
verifique então se elas são anagramas, ou seja, tem o mesmo conjunto de letras.
"""
#foi feito no python
string1 = input("Digite a primeira string: ").lower().replace(" ", "")
string2 = input("Digite a segunda string: ").lower().replace(" ", "")       #replace remove espaços em branco

if sorted(string1) == sorted(string2):                #A função sorted() converte cada string em uma lista ordenada de caracteres.
    print("As strings são anagramas!")
else:
    print("As strings NÃO são anagramas.")
