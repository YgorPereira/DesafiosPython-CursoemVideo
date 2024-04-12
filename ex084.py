# Cadastrando pessoas mostrando as mais leves e as pesadas

dados = list()
pessoas = list()
maior = menor = cont = 0

while True:
    print(30*'-=')
    dados.append(str(input('Digite o nome da pessoa: ')))
    dados.append(float(input('Digite o peso da pessoa: ')))   
    if cont == 0:
        maior = dados[1]
        menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    print('Cadastro realizado')
    cont = + 1
    dados.clear()
    stop = input('Você que continuar? [S/N]').upper().strip()
    while stop[0] not in 'SN':
        print('Respostra inválida...')
        stop = input('Você que continuar? [S/N]').upper().strip()
    if stop[0] == 'N':
        break

print(30* '-=')
print(f'Foram cadastradas {cont} pessoas...')

if menor == maior:
    print(f'O maior e menor peso foram iguais, {maior}kg, que é o peso das seguintes pessoas: ', end='' )
    for p in pessoas:
        if p[1] == maior:
            print(f'{p[0]} ', end='')
else:
    print(f'O maior peso foi {maior}kg, que é o peso das seguintes pessoas: ', end='')
    for p in pessoas:
        if p[1] == maior:
            print(f'{p[0]} ', end='')

    print(f'\nO mais leve foi {menor}kg, que é o peso das seguites pessoas: ')
    for p in pessoas:
        if p[1] == menor:
            print(f'{p[0]} ', end='')

