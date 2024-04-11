# lendo e cadastrando valores, ignorando os duplicados e mostrando os cadastrados em ordem crescente

valores = []

while True:
    valor = (int(input('Adicione um valor: ')))
    if valor in valores:
        print('Valor duplicado. Não irei cadatra-lo...')
    else:
        valores.append(valor)
    stop = input('Você quer continuar? [S/N]:').upper().strip()
    while stop[0] not in 'SN': 
        print('Resposta invalida: ')
        stop = input('Você quer continuar? [S/N]:').upper().strip()
    if stop[0] == 'N':
        break
valores.sort()
print(20 * '-=')
print(f'Os valores cadastrados foram: {valores}')