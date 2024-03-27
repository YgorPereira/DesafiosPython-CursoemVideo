reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))

if reta1 < reta2 + reta3 or reta2 < reta3 + reta1 or reta3 < reta1 + reta2:
    print('Isso é um triângulo.')
    if reta1 == reta2 == reta3:
        print('Esse triângulo é equilátero.')

    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print('Esse triângulo é isósceles')

    elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
        print('Esse triângulo é escaleno.')

else:
    print('Isso não é um triângulo.')

