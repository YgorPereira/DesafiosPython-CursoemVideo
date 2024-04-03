# calculando a média de idade, o homem mais velho, mulheres menos 20 anos

nome_velho = ''
idade_velho = 0
soma_idades = 0
soma_mulher = 0
for count in range(4):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))
    gen = str(input('Digite "H" se for homem ou "M" se for mulher: ')).strip().upper()
    soma_idades += idade
    media_idades = soma_idades / 4
    if count == 0 and gen == 'H':
        nome_velho = nome
        idade_velho = idade
    else:
        if gen == 'H' and idade > idade_velho:
            nome_velho = nome
    if gen == 'M' and idade < 20:
        soma_mulher += 1

print(f'A média de idades é {media_idades}')
print(f'O homem mais velho do grupo é {nome_velho}')
if soma_mulher == 1:
    print(f'Existe {soma_mulher}mulher com menos de 20 anos.')
else:
    print(f'Existem {soma_mulher}mulheres com menos de 20 anos.')
