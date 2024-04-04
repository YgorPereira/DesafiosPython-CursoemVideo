n = int(input('Digite um número inteiro: '))
soma = 0
count = 0
while n != 999:
    soma +=  n
    count += 1
    n = int(input('Digite um número inteiro: '))
print(f'Foram digitados {count} números e soma entre eles foi {soma}')