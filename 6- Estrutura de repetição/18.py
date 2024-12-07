cont1 = 0
cont2 = 0
brancos = 0
nulos = 0

while True:
    voto = int(input("Digite um voto (1 para candidato 1, 2 para candidato 2, 0 para branco, qualquer outro número para nulo, -1 para encerrar): "))
    
    if voto == -1:
        break
    elif voto == 1:
        cont1 += 1
    elif voto == 2:
        cont2 += 1
    elif voto == 0:
        brancos += 1
    else:
        nulos += 1

print("Votos para o candidato 1:", cont1)
print("Votos para o candidato 2:", cont2)
print("Votos brancos:", brancos)
print("Votos nulos:", nulos)
