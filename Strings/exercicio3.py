"""
Leia um código de cinco algarismos (variável Codigo) e gere o digito verificador (DigitoV) módulo 7 para o mesmo. 
Supondo que os cinco algarismos do código são ABCDE, 
uma forma de calcular o dígito desejado, com módulo 7 é:
"""

#Solicitar o código de 5 algarismos ao usuário
codigo = input("Digite um código de 5 algarismos: ")

# Garantir que o código tenha exatamente 5 dígitos
if len(codigo) == 5 and codigo.isdigit():
    # Extrair os algarismos
    A, B, C, D, E = map(int, codigo)
    
    # Calcular o valor de S
    S = 6 * A + 5 * B + 4 * C + 3 * D + 2 * E
    
    # Calcular o dígito verificador como o resto de S por 7
    DigitoV = S % 7
    
    # Exibir o resultado
    print(f"O dígito verificador (módulo 7) é: {DigitoV}")
else:
    print("Código inválido! Por favor, insira exatamente 5 dígitos.")