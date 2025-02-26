"""
Módulo mis_funciones
--------------------

Este módulo contiene dos funciones de ejemplo:
1. `calculadora`: realiza operaciones básicas (suma, resta, multiplicación y división).
2. `fibonacci`: calcula el término n de la sucesión de Fibonacci de manera recursiva.

Las pruebas unitarias de tipo doctest también se incluyen en los docstrings de cada función.
"""


def calculadora(a, b, operacion):
    """
    Realiza una operación aritmética básica (suma, resta, multiplicación, división)
    sobre dos números.

    Parámetros
    ----------
    a : float o int
        Primer número.
    b : float o int
        Segundo número.
    operacion : str
        Tipo de operación a realizar. Debe ser uno de los siguientes valores:
        "suma", "resta", "multiplicacion" o "division".

    Returns
    -------
    float
        El resultado de la operación realizada.

    Raises
    ------
    ValueError
        Si la operación no está entre las válidas.
    ZeroDivisionError
        Si se intenta realizar una división por cero.

    Ejemplos
    --------
    >>> calculadora(10, 5, "suma")
    15
    >>> calculadora(10, 5, "resta")
    5
    >>> calculadora(3, 4, "multiplicacion")
    12
    >>> calculadora(10, 2, "division")
    5.0
    >>> calculadora(10, 0, "division")  # Test para la excepción de división por cero
    Traceback (most recent call last):
    ...
    ZeroDivisionError: division by zero

    """
    if operacion == "suma":
        return a + b
    elif operacion == "resta":
        return a - b
    elif operacion == "multiplicacion":
        return a * b
    elif operacion == "division":
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return a / b
    else:
        raise ValueError("Operación no válida. Use 'suma', 'resta', 'multiplicacion' o 'division'.")


def fibonacci(n):
    """
    Devuelve el término n de la sucesión de Fibonacci de forma recursiva.

    La sucesión de Fibonacci se define como:
    - fibonacci(0) = 0
    - fibonacci(1) = 1
    - fibonacci(n) = fibonacci(n-1) + fibonacci(n-2) para n > 1

    Parámetros
    ----------
    n : int
        El índice del término de Fibonacci que se desea obtener. Debe ser un entero >= 0.

    Returns
    -------
    int
        El término n de la sucesión de Fibonacci.

    Raises
    ------
    ValueError
        Si n es un entero negativo.

    Ejemplos
    --------
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(10)
    55
    >>> fibonacci(-1)
    Traceback (most recent call last):
    ...
    ValueError: El valor de n no puede ser negativo.
    """
    if n < 0:
        raise ValueError("El valor de n no puede ser negativo.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
