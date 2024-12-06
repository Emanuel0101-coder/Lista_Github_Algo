"""
Dadas duas sequências com n números inteiros entre 0 e 9, interpretadas como dois números inteiros de n algarismos, 
calcular a sequência de números que representa a soma dos dois inteiros.
"""

"""
  1  8  2  4  3  4  2  5  1
+    3  3  7  5  2  3  3  7
  -------------------------
  2  1  6  1  8  6  5  8  8
"""

#Definindo as duas sequencias de numeros
A = [1, 8, 2, 4, 3, 4, 2, 5, 1]
B = [0, 3, 3, 7, 5, 2, 3, 3, 7]

#variaveis
resultado = []
inicio = 0
total = len(A)

#Somando as duas sequencias de trás para frente

for i in range(total - 1, -1, -1):
    soma = A[i] + B[i] + inicio
    resultado.append(soma % 10)         #O digito da soma
    inicio = soma // 10       #o "vai_um" (se houver)

#Se ainda houver um "vai um", adicionamos ao inicio
if inicio:
    resultado.append(inicio)

#Aqui um comando só para reverter a lista, já que ela está sendo executado da direita para a esquerda
resultado.reverse()
print(resultado)