#lendo vários números e mostrando em ordem decrescente, se o 5 foi econtrado entre eles e quantos fora digitados

valores = []
cont = 0

while True:
    valores.append(int(input('Digite um valor:')))
    cont = cont +1
    stop = str(input('Quer continuar? [S/N]: ')).upper().strip()
    while stop[0] not in 'SN':
        print('Resposta inválida...')
        stop = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if stop[0] == 'N':
        break
valores.sort(reverse= True)

print( 30 * '-=')
print(f'Foram digitados {cont} valores;')
print(f'Esses foram os valores digitados em ordem decrescente: {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
else: 
    print('O valor 5 não está na lista...')