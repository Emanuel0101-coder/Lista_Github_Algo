def torres_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover o disco 1 de {origem} para {destino}")
        return
    torres_hanoi(n-1, origem, auxiliar, destino)
    print(f"Mover o disco {n} de {origem} para {destino}")
    torres_hanoi(n-1, auxiliar, destino, origem)
def main():
    n = int(input("Digite o número de discos: "))
    torres_hanoi(n, 'Origem', 'Destino', 'Auxiliar')
if __name__ == "__main__":
    main()
