"""
Ler 100 números de matriculas de alunos e armazenar em um vetor. Esses números são distintos, ou seja, 
não existem números de matriculas iguais. Caso o usuário informa um número de matrículo que já existe, 
o programa deverá emitir um alerta.
"""

matricula = []

for c in range(100):
    num = int(input('Digite matricula: '))
    #vai percorrer se o numero digitado já existe no vetor
    if num in matricula:
        print('Esse valor de matricula já existe, digite outro numero')
    else:
        matricula.append(num)

print(matricula)
