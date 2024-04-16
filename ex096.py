def area():
    l = float(input('Digite a LARGURA do terreno (m): '))
    c = float(input('Digtie o COMPRIMENTO do terreno (m): '))
    a = l * c
    print(f'O terreno de largura {l:.2f} e comprimento {c:.2f} tem a área de {a:.2f}')


area()