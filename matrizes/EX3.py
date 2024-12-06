matrizA = [
    [-10, 1, 4, 6],
    [2, 3, 2, 8]
]
matrizB = [
    [1, 8, 4, -1],
    [0, 6, 3, -3]
]
soma = []

for i in range(len(matrizA)):
    linha_soma = []  
    for j in range(len(matrizA[i])):
        linha_soma.append(matrizA[i][j] + matrizB[i][j])  
    soma.append(linha_soma) 

for linha in soma:
    print(linha)

