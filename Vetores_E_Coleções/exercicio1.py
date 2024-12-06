"""
Fazer um algoritmo que calcule e imprima o soma, a média, o maior e o menor dos 
valores armazenados em um vetor A de 100 elementos
numéricos a serem lidos do dispositivo de entrada padrão.
"""

vet = []
soma = 0
maior = 0
menor = float('inf')         #aqui ela vai pegar o maior valor possivel, sendo garantido que vai ser menor o valor que entrar nesse if

for c in range(100):
    num = float(input('Digite numero: '))
    vet.append(num)

for num in vet:
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
media = soma / len(vet)
print(vet)
print(maior)
print(menor)
print(media)
print(soma)

