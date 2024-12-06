matrizA=[
    [-7,8],
    [4,9],
    [2,1]
]
transp=[]
for i in range (len(matrizA[0])):
    linha_transposta=[]
    for j in range(len(matrizA)):
        linha_transposta.append(matrizA[j][i])
    transp.append(linha_transposta)
for linha in transp:
    print(linha)