n = int(input('Digite um número inteiro [999]: '))
soma = 0
count = 0
while n != 999:
    soma +=  n
    count += 1
    n = int(input('Digite um número inteiro [999 para parar]: '))

if count == 0:
    print('Você não digitou nenhum número...')
    print('FIM')
else:
    print(f'Foram digitados {count} números e soma entre eles foi {soma}')