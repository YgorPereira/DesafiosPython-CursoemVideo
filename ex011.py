wall_a = float(input('Qual a altura da parede? '))
wall_l = float(input('Qual a largura da parede? '))

area = wall_a * wall_l
print(f'Sua parade tem uma dimensão de {wall_a} X {wall_l} área de {area:.2f}')

litros = area / 2
print(f'Derá necessário {litros:.150f}L de tinta para pinta-la.')
