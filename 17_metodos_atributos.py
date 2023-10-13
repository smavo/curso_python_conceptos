# Métodos y Atributos

# ¿Qué son los Métodos?
# La primera construcción que vamos a presentar que puede definirse dentro del cuerpo de la 
# clase son las funciones. **Cuando una función forma parte de una clase se le denomina método**. 

# Todo lo que hemos visto sobre las funciones se aplica también a los métodos, la única 
# diferencia práctica por ahora es la forma en que se invocan los métodos. 

class Coche:
    def velocidad_maxima():
        """Este método devuelve la velocidad máxima del coche."""
        print("Velocidad máxima: ???")

coche1 = Coche()


# ------------------------------------------------------------------------------

#  Parámetro selft
# Cuando definimos métodos en una clase es necesario proporcionarles el parámetro `self`, 
# que debe situarse en primer lugar antes de los otros parámetros. El parámetro `self` 
# es una referencia a la propia clase, y se utiliza para poder acceder a diferentes 
# componentes de la misma.

class Coche:
    def velocidad_maxima(self):
        """Este método devuelve la velocidad máxima del coche."""
        print("Velocidad máxima: ???")

coche1 = Coche()


# ------------------------------------------------------------------------------

# Acceso a los métodos de una clase

# Cuando instanciamos un objeto a partir de la clase, podemos acceder a los métodos con 
# la siguiente sintáxis: 
# <nombre_objeto>.<nombre_metodo>([<argumentos>])

class Coche:
    def velocidad_maxima(self):
        """Este método devuelve la velocidad máxima del coche."""
        print("Velocidad máxima: ??")

coche1 = Coche()

coche1.velocidad_maxima()


# ------------------------------------------------------------------------------

# ATRIBUTOS

# Otra de las cosas que podemos definir en una clase son variables. 
# **Cuando se define una variable dentro de una clase se denomina atributo**.

# A la hora de definir atributos en una clase, podemos definirlos de dos tipos: 
# **Atributos de clase** y **Atributos de instancia**.

# * Un **atributo de clase** es una variable que pertenece a la clase y va a estar 
# compartida entre todos los objetos que se instancien a partir de esa clase. 
# Podemos acceder al valor de estos atributos con la sintaxis:
# <nombre_objeto>.<nombre_atributo_clase>

class Coche:
    atributo_clase = 150
    
    def velocidad_maxima(self):
        """Este método devuelve la velocidad máxima del coche."""
        print("Velocidad máxima dentro de Def:", self.atributo_clase)

renault = Coche()
renault.velocidad_maxima()
print(renault.atributo_clase)

bmw = Coche()
bmw.velocidad_maxima()
print(bmw.atributo_clase)


# * Un **atributo de instancia** es una variable que pertenece a un objeto en particular 
# y que solo puede ser accedida en el contexto de ese objeto. 
# Estas variables deben definirse en un método especial denominado constructor y 
# representado por la sintaxis `__init__()`. 
# Podemos acceder al valor de estos atributos con la sintaxis:

# <nombre_objeto>.<nombre_atributo_instancia>


# ------------------------------------------------------------------------------

# 4. Método `__init__()`
# El método `__init__()` es un método especial que Python ejecuta automáticamente cada 
# vez que creamos una nueva instancia basada en esa clase. 
# Este método tiene dos guiones bajos iniciales y dos guiones bajos finales, 
# una convención que ayuda a evitar que los nombres de métodos por defecto de 
# Python entren en conflicto con los definidos por el usuario.

# El método `__init__()` se denomina constructor de la clase debido a que asigna valores 
# específicos del objeto que se esta instanciando.

class Coche:
    
    def __init__(self, vel_max, consumo_medio, marca):
        self.vel_max = vel_max
        self.con_medio = consumo_medio
        self.nombre_marca = marca 
    
    def velocidad_maxima(self):
        """Este método devuelve la velocidad máxima del coche."""
        print("Marca de Vehiculo", self.nombre_marca)
        print("Velocidad máxima:", self.vel_max)
        
    def consumo_medio(self):
        print("El consumo medio es:", self.con_medio)


toyota = Coche(200, 7, 'toyota')
toyota.velocidad_maxima()
toyota.consumo_medio()

bmw = Coche(250, 10, 'bmw')
bmw.velocidad_maxima()
bmw.consumo_medio()


# ------------------------------------------------------------------------------


class Vehiculo():
    """Esta clase representa un coche."""
    
    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.
        
        Argumentos posicionales:
        modelo -- string que representa el modelo del coche
        potencia -- int que representa la potencia en cv
        conumo -- int que representa el consumo en l/100km
        """
        self.modelo = modelo
        self.potencia = potencia
        self.consumo = consumo
        
    def especificaciones(self):
        """Muestra las especicificaciones del coche."""
        print("-----------------------------------")
        print("Modelo:", self.modelo,
             "\nPotencia: {} cv".format(self.potencia),
             "\nConsumo: {} l/100km".format(self.consumo))
        

# help(Vehiculo)

mercedes = Vehiculo("mercedes c200", 180, 7)
mercedes.especificaciones()


### 2. Atributos con valores por defecto
class Vehiculo1():
    """Esta clase representa un coche."""
    
    def __init__(self, modelo, potencia, consumo):
        """Inicializa los atributos de instancia.
        
        Argumentos posicionales:
        modelo -- string que representa el modelo del coche
        potencia -- int que representa la potencia en cv
        conumo -- int que representa el consumo en l/100km
        """
        self.modelo = modelo
        self.potencia = potencia
        self.consumo = consumo
        self.km_actuales = 0
        
    def especificaciones(self):
        """Muestra las especicificaciones del coche."""
        print("-----------------------------------")
        print("Modelo:", self.modelo,
             "\nPotencia: {} cv".format(self.potencia),
             "\nConsumo: {} l/100km".format(self.consumo),
             "\nKilometros actuales:", self.km_actuales)
        print("-----------------------------------")


camaro = Vehiculo1("camaro c200", 180, 7)
camaro.especificaciones()


### 3. Modificando los valores de los atributos de un objeto
# La manera más sencilla de modificar el valor de un atributo de un objeto es 
# utilizando la sintaxis: 
# <objeto>.<atributo> = <nuevo_valor>

camaro.km_actuales = -200
camaro.especificaciones()


# Por otro lado, existe una práctica mejor a la hora de modificar los atributos de la 
# clase que consiste en hacerlo a través de un método especialmente creado para ello.

# Esto nos permite realizar operaciones adicionales dentro de nuestro objeto siempre 
# que se recibe un nuevo valor de un atributo.

class Vehiculo2():
    """Esta clase representa un Vehiculo2."""
    
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
        print("-----------------------------------")
        print("Modelo:", self._modelo,
             "\nPotencia: {} cv".format(self._potencia),
             "\nConsumo: {} l/100km".format(self._consumo),
             "\nKilometros actuales:", self._km_actuales)
        
    def actualizar_kilometros(self, kilometros):
        print("-----------------------------------")
        """Actualiza los kilometros del coche."""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede establecer un numero de kilometros inferior al actual")

ferrari = Vehiculo2("ferrari c200", 180, 7)
ferrari.especificaciones()

ferrari.actualizar_kilometros(1000)
ferrari.especificaciones()



### 4. Extendiendo la funcionalidad de nuestra clase
class Vehiculo3():
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
        
    def actualizar_kilometros(self, kilometros):
        """Actualiza los kilometros del coche."""
        if kilometros > self._km_actuales:
            self._km_actuales = kilometros
        else:
            print("ERROR: No se puede establecer un numero de kilometros inferior al actual")
            
    def consumo_total(self):
        """Muestra el consumo total del coche desde el kilometro 0."""
        consumo_total = (self._km_actuales / 100) * self._consumo
        print("El consumo total es de {} litros".format(consumo_total))


mercedes = Vehiculo3("mercedes c200", 180, 7)
mercedes.consumo_total()
mercedes.especificaciones()
mercedes.actualizar_kilometros(100)
mercedes.consumo_total()

mercedes.actualizar_kilometros(250)
mercedes.consumo_total()
