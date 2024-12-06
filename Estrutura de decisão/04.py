
valemp = float(input('digite o valor do emprestimo: '))
num = int(input('digite o num de parcela: '))
sal = float(input('seu sal: '))
n = valemp / num
teto = sal * 0.30
if teto >= n:
    print('deu certo!!')
else:
    print('deu merda!!')