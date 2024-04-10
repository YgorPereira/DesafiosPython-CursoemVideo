#Lista de preços em tabulação:

lista = ('Pão', 0.50, 'Chocolate', 1.50, 'Leite', 2.50, 'Coxinha', 5.00, 'Pizza enrolada', 6.00, 'Bolo', 13.00 ) 
print(30*'-')
print('Tabela de preços')
print(30*'-')
for item in range(0 , len(lista)):
    if item % 2 ==0:
        print(f'{lista[item]:.<23}', end='')
    else:
        print(f'R${lista[item]:>5.2f}')
print(30*'-')