# contagem regressiva para ano novo

from time import sleep
import emoji

for count in range(10, -1, -1):
    print(count)
    sleep(1)
print(emoji.emojize('Feliz ano novo! :fireworks:'))
