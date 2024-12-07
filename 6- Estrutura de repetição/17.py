low = 1
high = 1000
tentativas = 0

print("Pense em um número de 1 a 1000.")
while tentativas < 10:
    palpite = (low + high) // 2
    print(f"É {palpite}? (acima/abaixo/certo): ")
    resposta = input().lower()
    tentativas += 1

    if resposta == "certo":
        print(f"Acertamos em {tentativas} tentativas!")
        break
    elif resposta == "acima":
        low = palpite + 1
    elif resposta == "abaixo":
        high = palpite - 1
else:
    print("Número não adivinhado em 10 tentativas.")
