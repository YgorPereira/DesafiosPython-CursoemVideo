# Programa principal
# def soma(a, b):
#     print('-' * 30)
#     print(f'A = {a}, B = {b}')
#     s = a + b
#     print(f'{a} + {b} = {s}')
#     print('-' * 30)

# soma(6, 4)

# contador
# def contador(*num):
#     len(num)
#     print(f'recebi os valores {num} e são ao todo {len(num)} números')


# contador(1, 2, 3, 4, 5, 6, 0, 2)

# trabalhando com lista
# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *= 2
#         pos += 1


# valores = [0, 1, 2, 3, 4, 5, 6]
# dobra(valores)
# print(valores)

# somando uma lista:
def soma (* valores):
    soma = 0
    for n in valores:
        soma += n
    print(f'A soma dos valores {valores} é igual {soma}')

soma(1, 2, 3, 5 )