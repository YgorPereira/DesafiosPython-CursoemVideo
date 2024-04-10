#Sorteando números e mostrando o maior e menor 

from random import randint
nums = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: ', end='')
for num in nums:
    print(f'{num} ', end='')
ordem_nums = sorted(nums)
print(f'\nO menor número sorteado foi {ordem_nums[0]}')
print(f'O maior número sorteado foi {ordem_nums[-1]}')
