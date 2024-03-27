from math import sqrt
co = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))

hip = co ** 2 + ca ** 2
hip = sqrt(hip)

print(f'Hipotenusa: {hip:.2f}')