#Mostrando a tabuda do número solicitado até o usuario digitar um valor negativo
print('TABUADA')
print(12 * '-=')
while True:
    n = int(input('Quer ver a tabuada de qual valor? [Digite um valor negativo para finalizar]: '))
    if n <= -1:
        break
  
    tabu = (f'''
{12 * '-'}
{n} X 1 = {n*1}
{n} X 2 = {n*2}
{n} X 3 = {n*3}
{n} X 4 = {n*4}
{n} X 5 = {n*5}
{n} X 6 = {n*6}
{n} X 7 = {n*7}
{n} X 8 = {n*8}
{n} X 9 = {n*9}
{n} X 10 = {n*10}
{12* '-'}''')
    print(tabu)
    
print('Finalizando...')

