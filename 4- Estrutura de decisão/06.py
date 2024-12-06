x = float(input('dig nota 01'))
z = float(input('dig nota 02'))
y = float(input('dig nota 03'))
q = float(input('dig nota 04'))

media = (x+z+y+q)/4
print(media)
if media >= 7:
    print('vc foi aprovada!!')
else:
    exame = float(input('dig sua nota exame'))
    nmedia = (media+exame)/2
    if nmedia >= 5:
        print('vc passou')
    else:
        print('reprovou')
