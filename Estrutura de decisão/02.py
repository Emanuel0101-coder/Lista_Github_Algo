x = int(input('N: '))
y = int(input('N: '))
z = int(input('N: '))

if x > y and x > z:
    print(x)
elif y > x and y > z:
    print(y)
elif z > x and z > y:
    print(z)
else:
    print('num iguais')