# Definindo o dicionário pessoas
# pessoas = {'nome': 'Ygor', 'idade': '18', 'sexo': 'M'}

# mostrando o nome de pessoas
# print(pessoas['nome'])

# mostrando o nome e a idade formatados
# print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos')

# mostrando os valores
# print(pessoas.values())

# mostrando as keys
# print(pessoas.keys())

# mostrando os itens
# print(pessoas.items())

# usando o laço for para mostrar as keys
# for k in pessoas.keys():
#     print(k)

# usando o laço for para os valores
# for v in pessoas.values():
#     print(v)

# usando o laço for para mostras os items
# for k, v in pessoas.items():
#     print(f'{k} é {v}')

# deletando a key idade
# del pessoas['idade']
# print(pessoas)

# alterando os valores
# pessoas['nome'] = 'Yago'
# pessoas['idade'] = 13
# print(pessoas)

# adicionando uma nova key com um valor
# pessoas['nova key'] = 'novo valor'
# print(pessoas)

# lendo valores e o adicionando e keys
# pessoas['nome'] = str(input('Digite um nome: '))
# pessoas['idade'] = int(input('Digite uma idade: '))
# pessoas['sexo'] = str(input('Digite o sexo: '))
# for k, v in pessoas.items():
#     print(f'{k} = {v}')

# criando uma lista e adicionando dicionários
# brasil = list()
# estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
# estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
# brasil.append(estado1)
# brasil.append(estado2)
# print(brasil) #mostrando toda a lista
# print(brasil[0]) #mostrando só o primeiro elemento de brasil
# print(brasil[0]['sigla']) #mostrando só a siglas do primeiro elemento

# lendo três uf e três siglas, fazendo uma cópias e os adicionando numa lista
# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = str(input('Digite uma uf: '))
#     estado['sigla'] = str(input('Digite a sigla da uf: '))
#     brasil.append(estado.copy())
# print(brasil)
