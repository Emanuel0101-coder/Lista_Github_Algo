def fibonacci(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)
def main():
    N = int(input("Digite um número inteiro positivo N para encontrar o N-ésimo termo da sequência Fibonacci: "))
    resultado = fibonacci(N)
    print(f"O {N}-ésimo termo da sequência Fibonacci é: {resultado}")
if __name__ == "__main__":
    main()
