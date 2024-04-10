# Indentificando vogais:

palavras = ('andar', 'dirigir', 'navegar', 'acessar', 'entrar', 'correr', 'nadar', 'comer', 'dormir')
for c in range(0, len(palavras)):
    print(f'\nNa palavra {palavras[c].upper()} as vogais são: ', end='')
    for letra in palavras[c]:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')