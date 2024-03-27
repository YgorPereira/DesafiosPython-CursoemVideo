dias = int(input('Dias alugados: '))
km = float(input('KMs rodados: '))
val_dias = dias * 60
val_km = km * (15/100)
val_total = val_km + val_dias
print(f'Valor a pagar: R${val_total:.2f}')