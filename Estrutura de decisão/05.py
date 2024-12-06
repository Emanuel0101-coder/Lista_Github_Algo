
valor = float(input('Valor venda: '))
if valor > 50000:
    sobra = valor * 0.12
    print(sobra)
elif valor >= 30000 and valor <= 50000:
    sobra = valor * 0.095
    print(sobra)
elif valor < 30000:
    sobra = valor * 0.07
    print(sobra)