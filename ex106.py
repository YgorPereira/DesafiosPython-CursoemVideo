def ajuda():
    print(f'''{30 * '~'}
{"SISEMA DE AJUDA":30}
{30 * '~'}''')
    while True:
        função = str(input('qual função ou biblioteca quer ver? (digite "fim" para sair) ')).strip().lower()
        print(f'''{30 * '~'}
{"ACESSANDO...":30}
{30 * '~'}''')
        help(função)
        print(30 * '-=')
        if função == "fim":
            print(f'''{30 * '~'}
{"ENCERRANDO...":30}
{30 * '~'}''')
            break

ajuda()