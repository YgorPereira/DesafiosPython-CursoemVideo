# Boletim com listas compostas

boletim = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota da prova 1: '))
    n2 = float(input('Nota da prova 2: '))
    media = (n1 + n2) / 2
    boletim.append([nome, [n1, n2], media])
    stop = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while stop[0] not in 'SN':
        stop = str(input('Resposta inválida...\nQuer continuar? [S/N]: ')).upper().strip()
    if stop == 'N':
        break
print(15 * '-=')
print(f'{'N°':<4}{'Nome':<10}{'Média':>5}')
print(30 * '-')
for c, p in enumerate(boletim):
    print(f'{c+1:<4}{p[0]:<10}{p[2]:>5}')
print(30 * '-')
