reta1 = float(input('Digite o tamanho da primeira reta: '))
reta2 = float(input('Digite o tamanho da segunda reta: '))
reta3 = float(input('Digite o tamanho da terceira reta: '))

if reta1 <= 0 or reta2 <= 0 or reta3 <= 0:
    print('\033[4;33mValores nulos ou negativos não são aceitos!')

elif reta1 >= reta2 + reta3 or reta2 >= reta3 + reta1 or reta3 >= reta1 + reta2:
    print('\033[1;31mIsso não é um triângulo')

else:
    print('\033[1;32mIsso é um triângulo')