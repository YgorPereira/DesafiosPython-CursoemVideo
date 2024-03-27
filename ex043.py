print('Calculador de IMC:')
alt = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt ** 2)
print(f'IMC: {imc:.1f}')

if imc < 18.5:
    ('Você está abaixo do peso.')

if imc >= 18.5 and imc < 25:
    print('Você está no peso ideal.')

if imc >= 25 and imc < 30:
    print('Você está acima do peso.')

if imc >= 30 and imc <= 40:
    print('Você está com obesidade.')

else:
    print('Você está com obesidade morbida.')