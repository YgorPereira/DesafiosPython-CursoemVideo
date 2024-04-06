# lendo idade e sexo de pessoas e gerando informações
print(f'''
{15 * '-'}
CADASTRAR
{15 * '-'}''')
soma_18anos = 0
soma_homens = 0
sub20_mulheres = 0
cont = 0
while True:
    stop = ' '
    idade = int(input('Sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Seu sexo [M/F]: ')).strip().upper()[0]
    print('Cadastro realizado com sucesso!')
    cont += 1
    if idade >= 18:
        soma_18anos = soma_18anos + 1
    if sexo == 'M':
        soma_homens += 1
    if sexo == "F" and idade < 20:
        sub20_mulheres += 1
    while stop not in 'SN:':
        stop = str(input('Você que continuar? [S/N]: ')).strip().upper()[0]
    print(15 * '-=')
    if stop == 'N':
        break

print(f'''
Você cadastrou {cont} pessoas, delas:
{soma_18anos} tem mais de 18 anos;
{soma_homens} são homens;
{sub20_mulheres} são mulheres com menos de 20 anos.''')
