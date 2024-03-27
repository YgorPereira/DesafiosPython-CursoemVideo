print('Calcule sua Média!')
n1 = float(input('Qual foi a sua primeira nota?'))
n2 = float(input('Qual foi a sua segunda nota?'))
m = (n1 + n2) / 2
print(f'Média: {m:.1f}')

if m < 5:
    print('\033[0;31mREPROVADO!')

elif m >= 5 and m <= 6.9:
    print('\033[0;33mRECUPERAÇÃO...')

else:
    print('\033[0;32mAPROVADO!')