def fatorial(n, show=False):
    """
    :param n: define o número que você quer fatorar
    :param show: define se você quer mostrar a fatoração ou só o resultado
    :return: retorna o resultado da fatoração
    Função criada por Ygor Pereira
    """
    fat = 1
    for num in range(n, 0, -1):
        fat *= num
        if show == True:
            if num > 1:
                print (f'{num} X ', end='')
            else:
                print(num, end='')
    return f' = {fat}'


print(fatorial(5, show=True))
help(fatorial)
