# Lendo um número inteiro e mostrando seu noome por extenso:

num_ext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('Digite um número:'))
c = 0

while num < 0 or num > 20:
    print('Valor Inválido')
    num = int(input('Digite um número:'))

print(f'Você digitou o número {num_ext[num]}.')
