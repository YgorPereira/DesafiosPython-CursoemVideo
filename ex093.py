jogador = dict()
gols = list()
total_gols = 0
jogador['nome'] = str(input('Digite o nome do jogador: '))
jogos = int(input(f'Quantos jogos o {jogador["nome"]} jogou?'))
for c in range(0, jogos):
    gol_partida = (int(input(f' Quantos jogos o {jogador["nome"]} na {c+1}° partida? ')))
    total_gols += gol_partida
    gols.append(gol_partida)
jogador['gols'] = gols
jogador['total'] = total_gols

print(30*'-=')
print(jogador)

print(30*'-=')
for k, v in jogador.items():
    print(f'O campo {k} tem o valor de {v}...')

print(30*'-=')
print(f'O jogador {jogador["nome"]} jogou ao todo {jogos} jogos:')
for i, v in enumerate(gols):
    print(f' => Na {i}° partida {jogador["nome"]} fez {v} gols.')
print(f'Somando um total {jogador["total"]}!')