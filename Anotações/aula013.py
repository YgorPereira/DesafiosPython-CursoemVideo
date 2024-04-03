# repetir o "oi" 10 vezes
for count in range (1, 11): #ATENÇÃO A CONTAGEM É FEITA ATÉ O NÚMERO ANTERIO AO COLOCADO NO RANGEZ
   print('oi')
print('FIM')

# contagem do 6 ao 1
for count in range(6, 0, -1):
    print(count)
print('FIM')


# contando até o número fornecido pelo usuário
n = int(input('Digite um número: '))
for count in range(0, n+1):
    print(count)
print('FIM')

# contando com o inicio, fim e passo fornecido pelo usuário
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: '))
p = int(input('Digite o passo: '))
for count in range(i, f+1, p):
    print(count)
print('FIM')

#soma de 5 valors dados pelo usuário 
soma = 0
for count in range(0, 5):
    n = int(input('Digite um valor:'))
    soma = soma + n
print(f'A soma é {soma}')