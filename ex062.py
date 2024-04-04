2# mostrando os termos que o usário quiser de uma PA com while

a1 = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
termo = int(input('Até qual termo você quer ver?'))
count = 0
while count != termo - 1:
    count += 1
    an = count * r
    a10 = a1 + an
print(f'O décimo termo da sua pa é {a10}')