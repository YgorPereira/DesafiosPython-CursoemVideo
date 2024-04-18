def notas(*provas, sit=False):
    ficha = dict()
    soma = maior = menor = 0
    ficha['total'] = len(provas)
    for i, n in enumerate(provas):
        soma += n
        if i == 0 or n >= maior:
            maior = n
        if i == 0 or n <= menor:
            menor = n
    ficha['maior'] = maior
    ficha ['menor'] = menor
    ficha['média'] = int(soma / len(provas))
    if ficha['média'] <= 5 and sit == True:
        ficha['situação'] = 'Reprovado'
    if 5 < ficha['média'] <= 7 and sit == True:
        ficha['situação'] = 'Em recuperação'
    if ficha['média'] > 7 and sit == True:
        ficha['situação'] = 'Aprovado'
    return ficha
    
print(notas(5, 5, 5, sit=True))
print(notas(10, 9, 8, sit=True))
print(notas(7, 5, 6, sit=True))
print(notas(8, 9, 7))
    