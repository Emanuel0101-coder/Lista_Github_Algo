jorna = int(input('dig horas trabalhadas: '))
sal = float(input('salario seu: '))
if jorna > 160:
    acr = jorna - 160
    extra = acr * 1.50
    print(extra)
    total = (sal * jorna)+ extra
    print(total)
else:
    T = sal * jorna
    print(T)
    