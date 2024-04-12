# Palpites da megasena

from random import randint
from time import sleep
jogos = []
palpite = []
print(30 * '--')
print('PALPITES DA MEGASENA')
print(30 * '--')
quant = int(input('Quantos jogos você quer que eu gere? '))
cont = 0
while cont < quant:
    for c in range(0, 6):
        num = randint(1, 60)
        if num not in palpite:
            palpite.append(num)
    palpite.sort()
    jogos.append(palpite[:])
    palpite.clear()
    cont += 1
print(10 * '-=', f'SORTEANDO {quant} JOGOS', 10*'-=')
for p in jogos:
    print(p)