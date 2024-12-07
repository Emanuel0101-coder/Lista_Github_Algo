soma = 0
for i in range(1, 51):
    numerador = 1000 - (i - 1) * 3 
    denominador = i  
    if i % 2 != 0: 
        soma += numerador / denominador
    else:  
        soma -= numerador / denominador
print(f"O resultado da sequência é: {soma}")
