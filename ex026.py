frase = input('Digite uma frase: ').upper().strip()
print(f'A letra a aparece na frase {frase.count('A')} vezes')
print(f'A primeira vez que a letra A aparece é na posição {frase.find('A') + 1}.')
print(f'A ultima vez que a letra A aparece na frase é na posição {frase.rfind('A') + 1}')