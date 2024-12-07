morangos = float(input("Digite a quantidade de morangos (em kg): "))
macas = float(input("Digite a quantidade de maçãs (em kg): "))

if morangos <= 5:
    valor_morango = morangos * 2.50
else:
    valor_morango = morangos * 2.20

if macas <= 5:
    valor_maca = macas * 1.80
else:
    valor_maca = macas * 1.50
total = valor_morango + valor_maca
if morangos + macas > 8 or total > 25:
    total *= 0.9 

# Exibindo o valor final
print(f"O valor a ser pago é: R$ {total:.2f}")