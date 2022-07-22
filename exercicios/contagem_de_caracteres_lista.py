def contar_caracteres(s):
    """Função que conta os caracteres

    Ex:
    >>> contar_caracteres('mateus')
    'a': 1.
    'e': 1.
    'm': 1.
    's': 1.
    't': 1.
    'u': 1.
    >>> contar_caracteres('Silva')
    a: 1
    i: 1
    l: 1
    s: 1
    v: 1

    :param s: string a ser contada

    """
    caracteres_ordenados = sorted(s)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}:{contagem} ')
            caracter_anterior = caracter
            contagem = 1
    print(f'{caracter_anterior}: {contagem}')


if __name__ == '__main__':

    contar_caracteres('arthur')
    print()
    contar_caracteres('silva')
