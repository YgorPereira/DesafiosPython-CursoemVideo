city = input('Digite o nome da cidade: ').strip()
city = city.upper()
city = city.split()
print(f'Existe SANTOS no primeiro nome da cidade? {'SANTO' in city[0]}')