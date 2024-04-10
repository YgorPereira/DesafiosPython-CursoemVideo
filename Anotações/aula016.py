#Definindo a tupla:
# lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata')

#Provando que é imutavel:
# lanche[2] = 'coxinha'

#Repetição sem mostrar a posição:
# for comida in lanche:
#     print(comida)

#Repetição mostrando a posição:
# for c in range (0, len(lanche)):
#     print(f'{lanche[c]} na posição {c}')
#mostrando tuplas na ordem 

# print(lanche[1:])
# print(lanche[:3])
# print(lanche[1:3])
# print (lanche[2])
# print(lanche)
# print(f'{len(lanche)} comidas! Quanta coisa!')
# print(sorted(lanche))

#Somando tuplas:
# a = (2, 3, 5)
# b = (6, 7, 8, 9)
# c = a + b 
# d = b + a

# print(c, d)

#Contando quantos vezes aparece um elemento:
# print(c.count(5))

#Mostrando a posição de um elemento:
# print(c.index(6))

#Deletando uma tupla:
# del(c)
# print(c)