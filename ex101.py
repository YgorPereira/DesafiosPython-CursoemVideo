nasc = int(input('Em que ano você nasceu? '))

def voto(nasc):
    from datetime import date
    atual = date.today().year
    idade = atual - nasc
    print(f'Com {idade} anos, seu voto é ', end='')
    if idade < 16:
        return 'negado'
    elif 16 <= idade < 18 or idade > 65:
        return 'opcional'
    else:
        return 'obrigatorio'

print(voto(nasc))