def jogador(nome='<desconhecido>', gols=0):
    print(f'o jogador {nome} fez {gols} gols na temporada')

n = str(input('Qual o nome do jogador? ')).strip()
g = str(input('Quantos gols ele fez no campeonato? '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    jogador(gols = g)
else:
    jogador(n, g)
