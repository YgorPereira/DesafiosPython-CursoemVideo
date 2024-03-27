preco = float(input('Preço do produto: R$'))
desc = float(preco * (5 / 100))
print(f'Valor do desconto: R${desc:.2f} ')

new_preco = float(preco - desc)
print(f'Novo valor: R${new_preco:.2f}')