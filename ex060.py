#MOSTRANDO O FATORIAL DE UM NÚMERO LIDO
num = int(input('Digite um número: '))
multi = num
while num != 1: 
    fat= num -1
    num = fat
    multi = multi * fat
print (f'O resultado da fatorial do número é {multi}')