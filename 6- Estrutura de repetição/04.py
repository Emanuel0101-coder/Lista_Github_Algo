n = int(input('Digite um numero: '))

for i in range(1, n + 1):
    print(f"\nTabuada do {i}:")
    for j in range(1, 11):  # A tabuada vai de 1 até 10
        print(f"{i} x {j} = {i * j}")