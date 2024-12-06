est_civil = str(input('informe a primeira letra: '))
est_civil = est_civil.upper()
if est_civil == 'S':
    print('Você é solteiro')
elif est_civil == 'C':
    print('Você é Casado')
elif est_civil == 'V':
    print('Você é Viúvo')
elif est_civil == 'D':
    print('Você é divorciado')
elif est_civil == 'E':
    print('Você é dEquitado')
else:
    print('error')