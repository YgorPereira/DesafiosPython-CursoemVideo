from datetime import date
print('Confederação Nacional de Natação')
nasc = int(input('Qual o ano do nascimento do atleta?'))
ano = date.today().year
idade = ano - nasc

if idade > 0 and idade <= 9:
    print('Nadador na categoria MIRIM')

elif idade > 9 and idade <= 14:
    print('Nadador na categoria INFANTIL')

elif idade > 14 and idade <= 19:
    print('Nadador na categoria JUNIOR')

elif idade == 20:
    print('Nadador na categoria SÊNIOR')

elif idade > 20:
    print('Nadador na categoria MASTER')