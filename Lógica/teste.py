def atravessar_rio():
    lado_a = ['lobo', 'ovelha', 'couve']  # Itens no lado A
    lado_b = []  # Itens no lado B
    barco = ''  # O que está no barco

    # Passo 1: O homem leva o lobo
    barco = 'lobo'
    lado_a.remove('lobo')
    lado_b.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")

    # Passo 2: Homem volta sozinho
    barco = ''
    lado_b.remove('lobo')
    lado_a.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")

    # Passo 3: Homem leva a ovelha
    barco = 'ovelha'
    lado_a.remove('ovelha')
    lado_b.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")

    # Passo 4: Homem traz o lobo de volta
    barco = 'lobo'
    lado_b.remove('ovelha')
    lado_a.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")

    # Passo 5: Homem leva a couve
    barco = 'couve'
    lado_a.remove('couve')
    lado_b.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")

    # Passo 6: Homem volta sozinho
    barco = ''
    lado_b.remove('couve')
    lado_a.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")

    # Passo 7: Homem leva o lobo
    barco = 'lobo'
    lado_a.remove('lobo')
    lado_b.append(barco)
    print(f"Lado A: {lado_a}, Lado B: {lado_b}, Barco: {barco}")


# Executar a função
atravessar_rio()
