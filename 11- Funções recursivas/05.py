def inverter_string(s):
    if len(s) <= 1:
        return s
    else:
        return inverter_string(s[1:]) + s[0]
def main():
    s = input("Digite uma string: ")
    resultado = inverter_string(s)
    print(f"A string invertida é: {resultado}")
if __name__ == "__main__":
    main()
