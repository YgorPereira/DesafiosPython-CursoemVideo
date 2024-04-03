# mostrando os 10 primeiros temos de uma PA

a1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
a10 = a1 + (10 * r)
for count in range(a1, a10, r):
    print(count, end=', ')
print('FIM ')
