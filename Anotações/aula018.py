# teste = list()
# teste.append('Gustavo')
# teste.append('40')
# # print(teste)
# galera = list()
# galera.append(teste[:])
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)
# print(galera)

# galera = [['Ygor', 18], ['Luana', 18], ['Geron', 19]]
# # print(galera[0][0])
# for p in galera:
#     print(p)
#     print(f'O Nome é: {p[0]}')
#     print(f'A idade é: {p[1]}')

galera = list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    galera.append(dado[:])
    dado.clear()
# print(galera)

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
    else: 
        print(f'{p[0]} é menor de idade')