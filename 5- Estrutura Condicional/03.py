cod = int(input('Digite o codigo um cliente comum (1), funcionário (2) ou vip (3): '))
valor = float(input('Digite o valor da compra: '))
if cod == 2:
    desc = valor * 0.10
    total = valor - desc
    print(total)
elif cod == 3:
    desc = valor * 0.05
    total = valor - desc
    print(total)
else:
    print(valor)