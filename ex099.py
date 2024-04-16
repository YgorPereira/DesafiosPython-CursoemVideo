def maior(*valores):
    maior = cont = 0
    for v in valores:
        if cont == 0:
            maior = v 
        else:
            if v > maior:
                maior = v
        cont += 1
    print(30 * '-=')
    print(f'{valores} foram informados {cont} valores.')
    print(f'O maior deles foi {maior}.')
    print(30 * '-=')

maior(10, 20, 50, 10)

maior(103, 523, 2913, 20212, 392, 391)