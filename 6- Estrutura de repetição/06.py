deposito = float(input("Digite o valor depositado: "))
juros = 0.005

for mes in range(1, 13):
    deposito += deposito * juros
    print(f"Saldo no mês {mes}: R${deposito:.2f}")