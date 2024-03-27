a = input('Digite algo: ')

print(f'Qual o tipo desse valor? {type(a)}')
print('Só tem espaços?', a.isspace())
print('É um numero?', a.isnumeric())
print(f'É alpha?', a.isalpha())
print(f'É alphanumerico?', a.isalnum())
print(f'Está em maiuscula?', a.isupper())
print(f'Está em minusculo?', a.islower())

