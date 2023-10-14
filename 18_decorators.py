
## Conceptos avanzados sobre funciones:
# En Python las funciones también se consideran objetos y como consecuencia de esto 
# se pueden asignar a una variable, almacenarlas en estructuras de datos 
# (listas, tuplas, diccionarios...) o incluso pasarlas como argumento de otras funciones.

def func():
    print("Demo de prueba")

var = func
var()


def func2(function):
    function()

func2(func)

# -----------------------------------------------------------------------------

# Decorators

## ¿Qué es un decorator?

# Los _decorator_ envuelven una función, modificando su comportamiento realizando 
# una combinación de todas las propiedades que hemos visto anteriormente.

def mi_funcion():
    print("Hola mundo!!")

def mi_decorator(func):
    def wrapper():
        print("Ejecucion antes de la llamada a la funcion")
        func()
        print("Ejecucion despues de la llamada a la funcion")
    return wrapper

mi_funcion_mod = mi_decorator(mi_funcion)
mi_funcion_mod()


# Podemos utilizar _decorators_ para modificar el comportamiento de una función que 
# programemos, por ejemplo, añadiendo condiciones que se evalúen antes de ejecutar 
# la función ya existente que no queremos modificar.

def funcion2():
    print("Hola mundo!!")

def mi_decorator2(func):
    def wrapper():
        if var < 5:
            func()
        else:
            print("No se puede ejecutar la funcion")
    return wrapper


function = mi_decorator2(funcion2)
var = 2
function()

var = 10
function()


# -----------------------------------------------------------------------------

### _Syntactic Sugar_

# La sintaxis que hemos utilizado en el apartado anterior para definir 
# el _decorator_ es bastante compleja, por ello, 
# Python nos proporciona una alternativa mucho más sencilla.

def mi_decorator(func):
    def wrapper():
        print("Ejecucion antes de la llamada a la funcion2")
        func()
        print("Ejecucion despues de la llamada a la funcion2")
    return wrapper

@mi_decorator
def mi_function():
    print("Hola mundo!!")

mi_function()


# -----------------------------------------------------------------------------

# _Decorators_ en las Clases
# Una de las cosas interesantes sobre los _decorators_ es que Python nos proporciona 
# varios definidos por defecto que podemos utilizar dentro de una clase.

# Uno de los _decorators_ más interesantes que podemos utilizar es `@property`, 
# que nos permite definir métodos en una clase para consultar y modificar un 
# atributo interno.

class Coche():
    """Esta clase representa un coche."""
    
    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.
        
        Argumentos posicionales:
        modelo -- string que representa el modelo del coche
        potencia -- int que representa la potencia en cv
        conumo -- int que representa el consumo en l/100km
        """
        self._modelo = modelo
        self._potencia = potencia
        self._consumo = consumo
        self._km_actuales = 0
        
    def especificaciones(self):
        """Muestra las especicificaciones del coche."""
        print("Modelo:", self._modelo,
             "\nPotencia: {} cv".format(self._potencia),
             "\nConsumo: {} l/100km".format(self._consumo),
             "\nKilometros actuales:", self._km_actuales)
        
    @property
    def kilometros(self):
        return self._km_actuales
        
    @kilometros.setter
    def kilometros(self, kilometros):
        """Actualiza los kilometros del coche."""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede establecer un numero de kilometros inferior al actual")
            
    def consumo_total(self):
        """Muestra el consumo total del coche desde el kilometro 0."""
        consumo_total = (self._km_actuales / 100) * self._consumo
        print("El consumo total es de {} litros".format(consumo_total))


bmw = Coche("bmw i3", 150, 6)
bmw.kilometros
bmw.kilometros = 500
bmw.especificaciones()

bmw.kilometros
bmw.kilometros = 200