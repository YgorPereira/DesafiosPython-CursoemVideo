#validando expressões pelo número de parentes
exp = input('Digite sua expressao: ')
abre_p = []
fecha_p = []

for v in exp:
    if v == '(':
        abre_p.append(v)
    elif v == ')':
        fecha_p.append(v)

if len(abre_p) == len(fecha_p):
    print('Sua expressão é válida')
else: 
    print('Sua expressão é inválida')