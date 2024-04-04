#ler o sexo de uma pessoa e só aceitar M ou F

sexo = str(input('Qual o seu sexo? [M/F]')).strip().upper()[0]
while sexo != 'M' and sexo != 'F': 
    sexo = str(input('Por favor, digite "M" ou "F".')).strip().upper()[0]

if sexo == 'M':
    print('Seu sexo é masculino...')
if sexo == 'F':
    print('Seu sexo é feminino...')