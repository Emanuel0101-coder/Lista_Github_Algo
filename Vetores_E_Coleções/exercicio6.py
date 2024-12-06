"""
Escrever um programa que lê um vetor com 20 números inteiros e os imprime na tela. Troque, a seguir, o 1º elemento com o último, 
o 2º com o penúltimo etc. até o 10º com o 11º e 
imprima na tela o vetor N assim modificado.
"""

# Lê o vetor com 20 números inteiros
vetor = []
for i in range(20):
    num = int(input(f"Digite número: "))
    vetor.append(num)
#comparar depois
print(vetor)

# Troca os elementos
for i in range(10):             # Só vai até 10, pois está trocando em pares
    vetor[i], vetor[19 - i] = vetor[19 - i], vetor[i]

# Imprime o vetor modificado
print(vetor)

