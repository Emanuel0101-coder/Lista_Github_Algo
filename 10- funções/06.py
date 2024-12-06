n = int(input('digite um número: '))
def primo(n):
    if n <= 1:
        return False  
    cont = 0
    for i in range(1, n + 1): 
        if n % i == 0:
            cont += 1
    if cont == 2: 
        return True
    else:
        return False
print(primo(n))
