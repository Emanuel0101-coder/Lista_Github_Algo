"""
Uma escola de samba recebeu como pontos pela alegoria os seguintes 5 valores inclusos no vetor Notas. 
Lembrando que a nota mais alta e a nota mais baixa são descartadas. 
Faça um programa que calcule a média final do quesito.
"""

Notas = [9.9, 9.7, 9.8, 10, 10]

#Inicializa tudo no mesmo lugar
maior = Notas[0]
menor = Notas[0]
soma = 0

for Nota in Notas:             #aqui basicamente vai percorrer a variavel Nota em Notas
    if Nota > maior:
        maior = Nota            #se for maior, ele adiciona em Nota
    if Nota < menor:
        menor = Nota            #Se for menor, ele adiciona em Nota
    soma += Nota                #vai somar todas as notas

#media sendo calculada tirando a maior nota e a menor, e dividindo pelo len  de notas - 2(que foram as notas descartadas)
media = (soma - maior - menor)/(len(Notas) - 2)  
print('A média é {}'.format(media))
print('A maior nota é {}'.format(maior))
print('A menor nota é {}'.format(menor))
