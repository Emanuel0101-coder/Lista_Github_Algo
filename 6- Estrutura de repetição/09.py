soma = 0
for i in range(1, 38): 
    numerador1 = 38 - i  
    numerador2 = 39 - i  
    denominador = i 
    termo = numerador1 * numerador2 / denominador
    soma += termo
print(f"O resultado da equação é: {soma}")
