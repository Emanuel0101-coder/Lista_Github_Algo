matrizA=[
    [-7,8],
    [4,9],
    [2,1]
]
matrizB=[
    [1,-2],
    [0,5],
    [4,1]
]
linhasA=len(matrizA)
colunasA=len(matrizA[0])
linhasB=len(matrizB)
colunasB=len(matrizB[0])
if colunasA != linhasB:
    print("O produto de A × B não é possível: número de colunas de A diferente do número de linhas de B.")
else:
    matrizC = [[0 for _ in range(colunasB)] for _ in range(linhasA)]
    
    for i in range(linhasA):
        for j in range(colunasB):
            for k in range(colunasA): 
                matrizC[i][j] += matrizA[i][k] * matrizB[k][j]
    
   
    print("Matriz C (A × B):")
    for linha in matrizC:
        print(linha)