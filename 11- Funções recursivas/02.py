def fatorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * fatorial(N - 1)
def main():
    N = int(input("Digite um número inteiro positivo N: "))
    resultado = fatorial(N)
    print(f"O fatorial de {N} é: {resultado}")
if __name__ == "__main__":
    main()
