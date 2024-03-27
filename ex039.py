from datetime import date
print('CHECAGEM DE IDADE DO ALISTAMENTO MILITAR')
ano_nasc = int(input('Qual o ano do seu nascimento? '))
ano = date.today().year

if ano - ano_nasc < 18:
    print(f'''\033[0;33mFique tranquilo, ainda não é hora de se alistar...
Ainda faltam \033[4;33m{18 - (ano - ano_nasc)} anos\033[0;33m.''')

elif ano - ano_nasc == 18:
    print('\033[1;032mEstá na hora de se alistar!')

else:
    print(f'''\033[1;31mJá passou da hora de se alistar! Se aliste IMEDIATAMENTE!'
\033[1;31mJá se passaram {ano - ano_nasc - 18} anos desde o seu ano de Alistamento!''')