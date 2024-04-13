cadastro = dict()
cadastrados = list()
soma = média = 0
while True:
    cadastro['nome']= str(input('Nome: '))
    cadastro['sexo']=str(input('Sexo [M/F]: ')).upper().strip()
    while cadastro['sexo'] not in 'MF':
        cadastro['sexo']=str(input('SEXO INVÁLIDO! Digite "M" ou "F" porfavor...\nSexo [M/F]: ')).upper().strip()
    cadastro['idade']=int(input('Idade: '))
    while cadastro['idade'] < 0:
        cadastro['idade']=int(input('IDADE INVÁLIDA! Valores menores do que zero não são aceitos...\nIdade: '))
    print('Cadastro realizado com sucesso!')
    cadastrados.append(cadastro.copy())
    stop = str(input('Você que continuar? [S/N] ')).strip().upper()
    soma +=cadastro['idade']
    while stop not in 'SN':
        stop = str(input('RESPOSTA INVÁLIDA! Digite "S" para sim ou "N" para não...\nVocê que continuar? [S/N]')).upper().strip()
    if stop == 'N':
        break  
print(cadastrados)
print(30 * '-=')
print(f'A) Ao todo temos {len(cadastrados)} cadastrados.')

média = soma / len(cadastrados)
print(f'B) A média de idade é {média:.2f}')

print('C) As mulheres cadastradas são ', end='')
for i in cadastrados: 
    if i['sexo'] in 'F':
        print(f'{i['nome']} ', end='')

print('\nD) As pessoas com a idade acima da média: ')
for i in cadastrados:
    if i['idade'] > média:
        print(f'Nome: {i["nome"]}; Sexo: {i["sexo"]}; Idade: {i["idade"]}')