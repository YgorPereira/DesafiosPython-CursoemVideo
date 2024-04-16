from time import sleep

def contagem(a, b, c):
    print(30 * '-')
    print(f'A contagem de {a} até {b} de {c} em {c}: ') 
    if c < 0:
        c *=-1
    if c == 0:
        c = 1   
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += c
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= c
    print(f'\nFIM!')
    print(30 * '-')

contagem(1, 10, 1)
contagem(10, 0, 2)

print('Agora personalize sua contagem!')
a = int(input('Início: '))
b = int(input('Fim: '))
c = int(input('Passo: '))

contagem(a, b, c)