"""
Dado uma frase informada pelo usuário, converta as letras minúsculas em maiúsculas e vice-versa.
Entrada: PalAVra
saída:   pALavRA
"""

frase = input("Digite uma frase: ")

#função join, vai pecorrer cada caractere da frase digitada
#Se o caractere for minúsculo (char.islower()), ele é convertido para maiúsculo (char.upper()).
#E se for maisculo, ele é convertido para minusculo
frase_invertida = ''.join(char.upper() if char.islower() else char.lower() for char in frase)

print("Saída:", frase_invertida)