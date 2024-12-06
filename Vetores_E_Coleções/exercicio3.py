"""
Faça um programa que some o conteúdo de dois vetores e armazene o resultado em um terceiro vetor.
"""

Vet1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
Vet2 = [2, 4, 6, 8, 10, 12, 14, 16]
Vet3 = []
i = 0
while i < len(Vet1) or i < len(Vet2):                #vai rodar enquanto houver elementos em alguns dos vetores
    if i <len(Vet1) and i < len(Vet2):                  #verifica se tem o índice i em ambos os vetores
        Vet3.append(Vet1[i] + Vet2[i])
    elif i < len(Vet1):                               #vê se só no Vet1 tem
        Vet3.append(Vet1[i])                           
    else:
        Vet3.append(Vet2[i])                            #Se não tiver no Vet1, ele vai para o else e adiciona o elemento do Vet2
    i += 1
print(Vet3)
