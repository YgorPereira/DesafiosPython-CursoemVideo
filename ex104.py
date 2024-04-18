def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! Valor inválido...')
        if ok == True:
            break
    return valor
        
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar {n}')