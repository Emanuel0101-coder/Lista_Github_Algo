n = int(input("Digite um número inteiro: "))
if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")