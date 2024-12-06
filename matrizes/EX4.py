matrizA = [
    [2, -3],
    [-1, 4]
]

oposta = []

for i in range(len(matrizA)):
    linha_oposta = []
    for j in range(len(matrizA[i])):
        linha_oposta.append(-matrizA[i][j]) 
    oposta.append(linha_oposta) 

for linha in oposta:
    print(linha)
