# Funcion operaciones matematicas
def operacionMat():
    print(2 + 2)  # Sumar matematicas
    print(3 - 2)  # restar matematicas
    print(4 * 2)  # multiplicar matematicas
    print(5 / 2)  # dividir matematicas
    print(6 % 2)  # modular matematicas#
    print(2 ** 3)  # Exponential
    print(3 // 2)  # Residual


# Funcion tipoDatos para revisar los tipos de datos
def tipoDatos():
    print(type("texto"))  # Tipo de datos str o texto
    print(type(1))  # Tipo de datos entero
    print(type(2.5))  # Tipo de datos float
    print(type(True))  # Tipo de datos boolean
    print(type([1, 2, 3]))  # Tipo de datos list
    print(type({"a": 1, "b": 2, "c": 3}))  # Tipo de datos dict
    print(type(1 + 3j))  # Tipo de datos nuemro coplejos
    print(type({1, 3, 4}))  # Tipo de datos Set
    print(type(None))  # Tipo de datos None
    print(type((1, 2, 3, 4)))  # Tipo de datos tuple

# Funcion Euclidean distance


def euclidean(x, y):
    eu = (x[0] - y[0])**2 + (x[1] - y[1])**2
    eu = (eu)**0.5
    return print('El valor euclidian es: ', eu)


operacionMat()
tipoDatos()
euclidean([2, 3], [10, 8])
