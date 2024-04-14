# lendo o desempenho de um jogador, adionando o num time e exibindo ao usuário utilizando dicionário e listas.

jogador = dict()
time = list()
gols = list()
total_gols = cod = 0

while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['cod'] = cod
    jogos = int(input('Número de jogos do jogador: '))
    for c in range(0, jogos):
        gol_partida = int(input(f'Quantos gols ele fez no {c+1}° jogo? '))
        gols.append(gol_partida)
        total_gols += gol_partida
    jogador['gols'] = gols[:]
    jogador['total'] = total_gols
    gols.clear()
    cod += 1
    total_gols = 0
    time.append(jogador.copy())
    stop = str(input('Quer continuar? [S/N] ')).upper().strip()
    while stop not in 'NS':
        stop = str(input('RESPOSTA INVÁLIDA! Digite "S" para sim e "N" para não...\nQuer continuar? [S/N] ')).upper().strip()
    if stop in 'N':
        break
print(time)
print(30 * '-=')
print(f'{"LEVANTAMENTO DO TIME":^60}')
print(60 * '-')
for k in jogador.keys():
    print(f'{k:<15}', end='')
print()
for k, v in enumerate(time):
    for j in v.values():
        print(f'{str(j):<15}', end='')
    print()
print(60 * '-')
while True:
    indiv = int(input('Digite o código do jogador para mostrar seum desempenho (999 para parar): '))
    while indiv < 0 or indiv > len(time):
        indiv = int(input('Código inválido!\nDigite o código do jogador para mostrar seum desempenho (999 para parar): '))
    if indiv == 999:
        break
    for i in time:
        if indiv == i['cod']:
            c = 1
            for g in i['gols']:
                print(60 * '-')
                print(f' Na {c}° partida  {i["nome"]} fez {g} gols')
                c += 1
            print(f' Totalizando {i["total"]} gols.')