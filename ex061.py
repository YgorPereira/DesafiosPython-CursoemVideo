# mostrando os 10 primeiros temos de uma PA com while

a1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
count = 0
while count < 9:
    count += 1
    an = count * r
    a10 = a1 + an
print(f'O décimo termo da sua pa é {a10}')