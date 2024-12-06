ordem = int(input("Informe a ordem do Triângulo de Pascal: "))
pascal = [[1 if j == 0 or j == i else 0 for j in range(ordem)] for i in range(ordem)]

for i in range(2, ordem):
    for j in range(1, i):
        pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

print("Triângulo de Pascal:")
for i in range(ordem):
    print(" " * (ordem - i), end="")
    for j in range(i + 1):
        print(f"{pascal[i][j]:<3}", end=" ")
    print()
