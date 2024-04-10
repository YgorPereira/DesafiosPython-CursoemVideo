#Fornecendo informações das tabelas de time do brasileirão:

times = ('Atlhetico-PR', 'Atlético-GO', 'Atlético-PR', 'Bahia', 'Botafogo', 'Corinthians', 'Criciúma', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'FLuminense', 'Fortaleza', 'Juventude', 'EC-Vitoria', 'Bragantino', 'Vasco da Gama', 'São Paulo', 'Internacional', 'Grêmio', 'Palmeiras')

print(30 * '-=')
print(f'Os times são {times};')
print(30 * '-=')
print(f'Os primeiros colocados da tabela são: {times[0:5]}')
print(30 * '-=')
print(f'Os últimos colocados da tabela são: {times[-4:]}')
print(30 * '-=')
print(f'Em ordem alfabética: {sorted(times)}')
print(30 * '-=')
print(f'O na 8° posição está o {times[16]}')
print(30 * '-=')