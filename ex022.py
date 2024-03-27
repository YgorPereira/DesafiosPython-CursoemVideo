nome = input('Digite o seu nome completo: ').strip()

print(f'Nome em maiúsculo: {nome.upper()}')
print(f'Nome em minusculo: {nome.lower()}')
print(f'Número de caracteres no nome: {len(nome.replace(' ', ''))}')
print(f'Número de caracteres no primeiro nome: {len(nome.split()[0])}')