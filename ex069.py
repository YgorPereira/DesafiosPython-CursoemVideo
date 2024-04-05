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
    idade = int(input('Sua idade: '))
    if idade <= 0:
        print('Valor inválido.')
        idade = int(input('Sua idade: '))
    sexo = str(input('Seu sexo [H/F]: ')).strip().upper()
    if sexo not in 'HF':
        print('Valor inválido.')
        sexo = str(input('Seu sexo [H/F]: ')).strip().upper()
    print('Cadastro realizado com sucesso!')
    cont += 1
    if idade >= 18:
        soma_18anos = soma_18anos + 1
    if sexo in 'Hh':
        soma_homens += 1
    if sexo == "F" and idade < 20:
        sub20_mulheres += 1
    stop = str(input('Você que continuar? [S/N]: ')).strip().upper()
    print(15* '-=')
    if stop not in 'SN' or stop == '':
        print('Valor inválido.')
        stop = str(input('Você quer continuar? [S/N]: ')).strip().upper()
        print(15* '-=')
    if stop == 'N':
        break

print(f'''
Você cadastrou {cont} pessoas, delas:
{soma_18anos} tem mais de 18 anos;
{soma_homens} são homens;
{sub20_mulheres} são mulheres com menos de 20 anos.''')
