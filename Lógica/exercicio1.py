"""
Um homem precisa atravessar um rio com um barco que possui capacidade de transportar apenas ele e mais uma de suas três cargas, 
que são: um lobo, uma ovelha e um kilo de couve. 
Quais os passos que o homem deve fazer para conseguir atravessar o rio sem perder as suas cargas?
"""

"""
Primeira viagem: O homem leva a ovelha para o outro lado do rio.
Segunda viagem: Ele volta sozinho para o lado inicial.
Terceira viagem: O homem leva o lobo para o outro lado do rio.
Quarta viagem: Ele traz a ovelha de volta para o lado inicial.
Quinta viagem: O homem leva a couve para o outro lado do rio.
Sexta viagem: Ele volta sozinho para o lado inicial.
Sétima viagem: O homem leva a ovelha para o outro lado do rio.
"""

#codigo
def atravessar_rio():
    lado_a = ['lobo','ovelha','couve']  #Itens do lado A
    lado_b = [] #itens do lado b
    barco = ''  #o barco :D

    #Passo 1: O homem leva o lobo
    barco = 'lobo'
    lado_a.remove('lobo')
    lado_b.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

    #Passo 2: Homem volta sozinho
    barco = ''
    lado_b.remove('lobo')
    lado_a.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

    #Passso 3: Homem leva ovelha
    barco ='ovelha'
    lado_a.remove('ovelha')
    lado_b.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

    #Passo 4: Homem tras o lobo de volta
    barco = 'lobo'
    lado_b.remove('ovelha')
    lado_a.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

    #Passo 5: Homem leva a couve
    barco = 'couve'
    lado_a.remove('couve')
    lado_b.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

    #Passo 6: Homem volta sozinho
    barco = ''
    lado_b.remove('couve')
    lado_a.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

    #Passo 7: Homem leva o lobo
    barco = 'lobo'
    lado_a.remove('lobo')
    lado_b.append(barco)
    print('Lado A: {}, Lado B: {}, Barco: {}'.format(lado_a, lado_b, barco))

#executar
atravessar_rio()