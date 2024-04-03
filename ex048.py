# Soma dos números impáres multiplos de 3 entre 1 e 500

soma = 0
cont = 0
for count in range(1, 501, 2):
    if count % 3 == 0:
        soma += count
        cont += 1
print(f"existem {cont} números ímpares multiplos de 3 entre 1 e 500 e sua soma é {soma}, ")
