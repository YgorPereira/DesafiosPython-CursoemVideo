#Lendo números e fornecendo informações:

n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))
n3 = int(input('Digite o 3° valor: '))
n4 = int(input('Digite o 4° valor: '))
nums = (n1, n2, n3, n4)
if 9 not in nums:
    print('O número 9 não apareceu nenhuma vez.') 
else:
    print(f'O número 9 apareceu {nums.count(9)} vezes.')

if 3 not in nums:
    print('O número 3 não apareceu nenhuma vez.')
else:
    print(f'O número 3 apareceu pela primeira vez na posição {nums.index(3)+1}')

print('Os números pares são:')
for n in nums:
    if n % 2 == 0:
        print(n, end= ' ')