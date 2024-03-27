from random import randint
num = randint(1, 5)
print('A máquina pensou num número de 1 até 5.')
user_tent = int(input('Qual foi o número que máquina pensou? '))

if user_tent == num:
    print('\033[1:32mVocê acertou! Parabéns')
else:
    print('\033[1;31mInfelizmente você errou...')
print('--FIM--')
