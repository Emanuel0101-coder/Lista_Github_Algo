"""
Escreva um programa que, a partir de um nome informado pelo usuário, exiba suas iniciais. 
As iniciais são formadas pela primeira letra de cada nome, sendo que todas deverão aparecer em maiúsculas na saída do programa. 
Note que os conectores e, do, da, dos, das, de, di, du não são considerados nomes e, portanto, não devem ser considerados para a 
obtenção das iniciais. As iniciais devem ser impressas em maiúsculas, 
ainda que o nome seja entrado todo em minúsculas.
"""

#Essa função vai extrair as iniciais do nome fornecido pelo usuário, 
#ignorando palavras que são conectores (como de, do, da).
def obter_iniciais(nome):
    conectores = {'e', 'do', 'da', 'dos', 'das', 'de', 'di', 'du'}
    return ''.join(palavra[0].upper()               
    for palavra in nome.split()                     #aqui cria uma lista separando o texto por espaços, usando o split()
     if palavra.lower() not in conectores)

nome_usuario = input("Digite um nome completo: ")
print("Iniciais:", obter_iniciais(nome_usuario))
