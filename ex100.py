from random import randint
from time import sleep

numeros = list()

def sorteia(lista):
    print(f'Os cinco números sorteados foram: ', end='') 
    for cont in range(0, 5):
        num = (randint (0, 10))
        lista.append(num)
        cont += 1
        print (f'{num} ', end='', flush=True)
        sleep(0.5)


def somaPar(lista):
    soma = 0 
    for n in lista:
        if n % 2 == 0:
            soma += n 
    print(f'\nA soma dos valores pares entre {lista} é igual a: {soma}')


sorteia(numeros)
somaPar(numeros)