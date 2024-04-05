# Até qual termo você que ver na sequência de fibonacci 

n = int(input('Até qual termo de fibonacci você quer ver? '))
t1 = 0
t2 = 1  
print(f'{t1} - {t2}', end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print(f' - {t3}', end='')  
    t1 = t2
    t2 = t3
    count += 1
print(' - FIM')