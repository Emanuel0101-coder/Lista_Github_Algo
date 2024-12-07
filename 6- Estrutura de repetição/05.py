A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
soma = 0
for i in range(A + 1, B): 
    if i % 2 == 0:
        soma += i ** 3  
print(f"A soma dos cubos dos números pares entre {A} e {B} é: {soma}")
