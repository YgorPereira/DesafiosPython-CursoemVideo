from math import radians, cos, sin, tan
ang = float(input('Digite o valor do ângulo: '))
cos = cos(radians(ang))
sen = sin(radians(ang))
tang = tan(radians(ang))

print(f'O cosseno do ângulo {ang:.2f} é {cos:.2f}.')
print(f'O seno do ângulo {ang:.2f} é {sen:.2f}.')
print(f'A tangento do ângulo {ang:.2f} é {tang:.2f}.')
