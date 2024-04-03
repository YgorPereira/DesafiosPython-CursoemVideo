# calcular maioridade de 7 pessoas
from datetime import date

soma_maior = 0
soma_menor = 0
for count in range(0, 7):
    nasc = int(input(f'ano de nascimento da {count+1}° pessoa: '))
    idade = date.today().year - nasc
    if idade >= 18:
        soma_maior += 1
    else:
        soma_menor += 1
print(f'Dessa pessoas, {soma_maior} são de maior e {soma_menor} são de menor.')
