#lendo e adicionando 5 número numa lista, encontrando o maior e menor, e mostrando sua posição e seu valor

valores = []

for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

print(f'Os valores digitados na lista foram: ')
for p, v in enumerate(valores):
    print(f'{v}, ', end='')
    if p == 0:
        maior = v
        menor = v
        p_maior = p
        p_menor = p
    else:
        if v == maior:
            p_maior = [p_maior, p]
        if v == maior:
            p_menor = [p_menor, p]
        if v > maior:
            maior = v
            p_maior = p
        if v < menor:
            menor = v
            p_menor = p
        
print(f'\nO maior valor foi {maior} e ele está nas posições: {p_maior}')
print(f'O menor valor foi {menor} e ele está nas posições: {p_menor}')
