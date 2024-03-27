print('Olá! Vamos comparar dois números.')
num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))

if num1 > num2:
    print('\033[1;032mO primeiro valor é maior!')

elif num2 > num1:
    print('\033[1;33mO segundo valor é maior!')

else:
    print('\033[1;34mNão existe valor maior, pois eles são iguais!')