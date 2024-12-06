sala = float(input('informe seu salario: '))
sal = 1500
if sala < sal*3:
    print('vc ganha até tres salarios minimos')
    rea = sala * 1.50
    print(rea)
elif sala > sal*3 and sala < sal*10:
    print('vc ganha entre três até dez salários mínimo')
    rea = sala * 1.20
    print(rea)
elif sala > sal*20:
    print('vc ganha acima de dez até vinte salários mínimos')
    rea = sala * 1.15
    print(rea)
else:
    print('não entra nos criterios')
    rea = sal * 1.10
    print(rea)