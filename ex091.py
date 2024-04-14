# jogo de dados utilizando dicionário e lista.

from time import sleep
from random import randint
from operator import itemgetter

ranking = list()
rodada = {'jogador 1': randint(1, 6),
          'jogador 2': randint(1, 6),
          'jogador 3': randint(1, 6),
          'jogador 4': randint(1, 6)}
for k, v in rodada.items():
    print(f'{k} tirou {v}...')
    sleep(1)
ranking = sorted(rodada.items(), key=itemgetter(1), reverse=True)
print(15 * '-=')
print(f'{"==RANKING==":^30}')
for i, r in enumerate(ranking):
    print(f'{i+1}°: {r[0]} = {r[1]}')
