from random import choice
print('Jokenpô:')
jok= ['tesoura', 'papel', 'pedra']
user = int(input('Digite 1 para papel, 2 para tesoura e 3 para pedra: '))
pc= choice(jok)

if user == 1:
    print('Você jogou papel')
    print(f'O computador jogou {pc}')
    if pc == 'pedra':
        print('Jogador ganhou! Parabéns!')
    if pc == 'papel':
        print('Empatou!')
    else:
        print('O computador ganhou!')

if user == 2:
    print('Jogador jogou tesoura')
    print(f'O computador jogou {pc}')
    if pc == 'papel':
        print('Jogador ganhou! Parabéns!')
    if pc == 'tesoura':
        print('Empatou!')
    else:
        print('O computador ganhou!')

if user == 3 :
    print('Jogador jogou pedra')
    print(f'O computador jogou {pc}')
    if pc == 'tesoura':
        print('Você ganhou! Parabéns!')
    if pc == 'pedra':
        print('Empatou!')
    else:
        print('O computador ganhou!')

print('FIM')