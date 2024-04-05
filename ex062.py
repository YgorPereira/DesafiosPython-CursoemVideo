# mostrando os termos que o usário quiser de uma PA com while
n = int(input('Digite o primeiro termo da sua PA: '))
r = int(input('Digite a razão da sua PA: '))
termo = 0
mais = 10
count = 1
while mais != 0:
    termo += mais
    while count <= termo:
        print (f'{n} - ', end='')
        n += r
        count += 1
    print('PAUSA')
    mais = int(input('Quanto termos mais vc quer mostrar? '))
print('FIM')