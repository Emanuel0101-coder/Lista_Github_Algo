"""
Faça um programa que:

- Leia um vetor A com N elementos já ordenados e um vetor B com M elementos também já ordenados.
- Intercale os dois vetores A e B, formando um vetor C, sendo que ao final do processo de intercalação, o vetor C continue ordenado. 
- Nenhum outro processo de ordenação poderá ser utilizado além da intercalação dos vetores A e B.
- Caso um vetor (A ou B) termine antes do outro, o vetor C deverá ser preenchido com os elementos do vetor que ainda possui 
nformações.
"""

A = [1, 2, 3, 4, 5]
B = [2, 4, 6, 10, 12, 14, 16, 18]
C = []

#índices para percorrer A e B
i = 0 
j = 0

#Intercala os dois vetores enquanto houver elementos em ambos
while i < len(A) and j < len(B):
    if A[i] <= B[j]:
        C.append(A[i])  #Adiciona o índice i de A em C
        i += 1          #Move o índice de A para o próximo elemento
    else:
        C.append(B[j])  #Adiciona o índice j de B em C
        j += 1          #Move o índice de B para o próximo elemento

#Se sobrar elementos em A, adicione-os a C
C.extend(A[i:])  #Adiciona o restante de A, se houver

#Se sobrar elementos em B, adicione-os a C
C.extend(B[j:])  #Adiciona o restante de B, se houver

print(C)

