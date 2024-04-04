#jogo para o usuario acertar o número aleatória de 1 a 10 que foi pensado pela máquina

from random import randint

print('---TENTE ACERTAR O NÚMERO---')

num = randint(0, 10)
print('A máquina pensou num número de 0 a 10...')
user_tent = int(input('Qual o número você acha que a máquina pensou? '))
count = 1

while user_tent != num:
    count += 1
    print('Você errou. Tente novamente...')
    if  user_tent < num:
        print('O número é maior que esse...')
    if  user_tent > num:
        print('O número é menor que esse...')
    user_tent = int(input('Qual o número você acha que a máquina pensou? '))
    
 
print(f'Parabéns, você acertou! o número era {num}...')
print(f'Foram necesárias {count} tentativas para você acertar.')