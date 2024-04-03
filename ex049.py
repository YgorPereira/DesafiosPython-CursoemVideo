#tabuada de um número que o usuário colocar usando for

n = int(input('Digite um número: '))
for count in range (1, 11):
    print(f'{n} X {count} = {n * count}')

print('FIM')