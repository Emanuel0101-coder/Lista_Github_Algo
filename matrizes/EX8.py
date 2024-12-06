matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

90 = [[matriz[j][i] for j in range(len(matriz)-1, -1, -1)] for i in range(len(matriz[0]))]

180 = [linha[::-1] for linha in matriz[::-1]]

270 = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0])-1, -1, -1)]

print("Rotação 90°:")
for linha in 90:
    print(linha)

print("\nRotação 180°:")
for linha in 180:
    print(linha)

print("\nRotação 270°:")
for linha in 270:
    print(linha)
