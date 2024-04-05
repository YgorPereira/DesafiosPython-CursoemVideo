# mostrando os 10 primeiros temos de uma PA com while
a1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
n = a1
count = 1
while count <= 10:
    print (f'{n} - ', end='')
    n += r
    count += 1
print('FIM')