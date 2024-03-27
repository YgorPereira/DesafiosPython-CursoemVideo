import calendar
year = int(input('Digite um ano: '))
if calendar.isleap(year):
    print('\033[1;32mEsse ano é bissexto.')
else:
    print('\033[1;31mEsse ano não é bissexto.')