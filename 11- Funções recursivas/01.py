def somatorio(N):
    if N == 1:
        return 1
    else:
        return N + somatorio(N - 1)
def main():
    N = int(input("Digite um número inteiro positivo N: "))
    resultado = somatorio(N)
    print(f"O somatório de 1 até {N} é: {resultado}")


if __name__ == "__main__":
    main()
