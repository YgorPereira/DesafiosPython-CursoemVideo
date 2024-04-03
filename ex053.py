# verificando se a frase é um palindromo

frase = str(input('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto= ''.join(palavras)
reverso =''
for letra in range(len(junto)-1, -1, -1):
    reverso += junto[letra]
print(f'a frase ao inverso é "{reverso}".')
if junto== reverso:
    print ('A frase é um palíndromo')
else:
    print ('A frase não é um palíndromo')