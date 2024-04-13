from datetime import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
trabalhador['Idade'] = datetime.now().year - nasc
trabalhador['CTPS'] = int(input('Carteira de Trabalho (se não tem, digite 0): '))
if trabalhador['CTPS'] > 0:
    trabalhador['Ano de contratação'] = int(input('Ano de contratação: '))
    trabalhador['Salário'] = float(input('Salário: R$'))
    trabalhador['Aposentadoria'] =( (trabalhador['Ano de contratação'] + 35) - datetime.now().year) + trabalhador['Idade']
print(30 * '-=')
for k, v in trabalhador.items():
    print(f'{k}: {v}')
