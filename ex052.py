# lendo um número e dizendo se ele é primo ou não

n = int(input('Digite um valor: '))
tot = 0
for count in range(1, n+1):
    if n % count == 0:
        tot+=1
print(f'O número foi divisível por {tot} números;')
if tot == 2:
    print('Logo ele é um número primo.')
else:
    print('Por isso ele não é um número primo.')
