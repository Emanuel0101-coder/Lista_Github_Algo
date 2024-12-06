combustivel = str(input('escreva a forma que vc abasteceu: '))

if combustivel == 'GASOLINA':
    qtd = float(input('digite a quantidade: '))
    if qtd <= 20:
        desc = qtd * 0.3
        print(desc)
        valor = (3.3 * qtd) - desc
        print(valor)
    elif qtd > 20:
        desc = qtd * 0.5
        print(desc)
        valor = (3.3 * qtd) - desc
        print(valor)
else:
    qtd = float(input('digite a quantidade: '))
    if qtd <= 20:
        desc = qtd * 0.4
        print(desc)
        valor = (2.9 * qtd) - desc
        print(valor)
    elif qtd > 20:
        desc = qtd * 0.6
        print(desc)
        valor = (2.9 * qtd) - desc
        print(valor)
