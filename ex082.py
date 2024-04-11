#Criando uma lista de número e dividindo em pares e impares:

valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    stop = input('Você quer continuar? ').upper().strip()
    while stop[0] not in 'SN':
        print('Resposta inválida...')
        stop = input    ('Você quer continuar? ').upper().strip()
    if stop[0] == 'N':
        break
for v in valores:
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)

print(f'Todos os valores são: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')

