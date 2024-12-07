numeros = []
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

pares = [x for x in numeros if x % 2 == 0]
impares = [x for x in numeros if x % 2 != 0]

print(f"Maior: {max(numeros)}")
print(f"Menor: {min(numeros)}")
print(f"Soma: {sum(numeros)}")
print(f"Média: {sum(numeros)/len(numeros):.2f}")
print(f"Pares: {len(pares)}")
print(f"Ímpares: {len(impares)}")