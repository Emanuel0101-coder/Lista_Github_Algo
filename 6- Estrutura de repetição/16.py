n = int(input("Digite um número: "))
fibonacci = [0, 1]

while fibonacci[-1] <= n:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print("Sequência:", fibonacci[:-1])