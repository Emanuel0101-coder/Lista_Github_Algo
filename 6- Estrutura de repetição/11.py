massa = float(input("Digite a massa inicial (g): "))
tempo = 0

while massa >= 0.05:
    massa /= 2
    tempo += 50

print(f"O tempo necessário é: {tempo} segundos.")