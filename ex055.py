# lendo pesos de 5 pessoas e mostrando o maior e menor
maior = 0
menor = 0
for count in range(5):
    peso = float(input(f'Digite o peso da pessoa: '))
    if count == 1:
        maior = peso
        menor = peso 
    else:
        if peso > maior: 
            maior = peso
        elif peso < menor:
            menor = peso

print(f'Maior peso: {maior}')
print(f'Menor peso: {menor}')
