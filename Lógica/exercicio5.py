"""
Um palíndrome é um número inteiro positivo, sem zeros à esquerda, que é o mesmo se lido da esquerda para a 
direita ou da direita para a esquerda. Por exemplo, os números 11 e 65256 são palíndromes, mas os números 010 e 123 não são. 
A diferença entre o valor do maior palíndrome de três dígitos e o menor palíndrome de três dígitos é:
1 - 989
2 - 888
3 - 898
4 - 998
5 - 979
"""

#Resposta: 898, já que o maior palindrome é 999, e o menor seria 101, se subtrairmos esses dois fica:
palindromeDiferença = 999 - 101
print(palindromeDiferença)