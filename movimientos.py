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
<<<<<<< HEAD
    nombre=input()
    p = 'Peon blanco'
    t = 'torre blanco'
    k = 'caballo blanco'
    a = 'alfil blanco'
    q = 'reina blanco'
    r = 'rey blanco'
    P='Peon negro'
    T='Torre negra'
    K='Caballo negro'
    A='Alfil negro'
    Q='Reina negra'
    R='Rey negro'
    vacio=""
    return ('su ficha es',nombre)



=======
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
>>>>>>> db01fb536b753498c71fd8395c7b4ecf23970bab
