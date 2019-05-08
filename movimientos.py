def tablero_a_cadena(tablero):
    cadena = ""
    for fila in tablero:
        cadena += str(fila) + "\n"
    return cadena


def obtener_nombre_pieza(simbolo):
    """
    (str) -> str

    >>> obtener_nombre_pieza('p')
    'Peon blanco'
    >>> obtener_nombre_pieza('R')
    'Rey Negro'

    Retorna el nombre de la pieza del ajedrez dado su simbolo

    :param simbolo: la representacion de la pieza segun el enunciado
    :return: El nombre y color de la pieza
    """

    tipo = 'Negro'
    if simbolo.islower():
        tipo = 'blanco'
    retorno = simbolo.lower()
    if retorno == 'p':
        return 'Peon '+tipo
    elif retorno == 't':
        return 'Torre ' + tipo
    elif retorno == 'k':
        return 'Caballo ' + tipo
    elif retorno == 'a':
        return 'Alfil ' + tipo
    elif retorno == 'q':
        return 'Reina ' + tipo
    elif retorno == 'r':
        return 'Rey ' + tipo
    else:
        return 'No es una pieza'

def mover_torre(tablero, x_inicial, y_inicial, x_final, y_final):
    """
    >>> mover_torre(tablero[[]],0,0,1,0)

    :param tablero:
    :param x_inicial:
    :param y_inicial:
    :param x_final:
    :param y_final:
    :return:
    """
    tablero = [
        ['t', 'k', 'a', 'q', 'r', 'a', 'k', 't'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['T', 'K', 'A', 'R', 'Q', 'A', 'K', 'T']
    ]
    if x_inicial == x_final or y_inicial == y_final:
        if tablero[x_inicial][y_inicial].lower() == 't' :
            for y in range(y_inicial,y_final-1):
                if tablero[x_inicial][y]!=" ":
                    break




