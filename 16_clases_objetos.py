
# Clases en Python 

## Orientacion a Objetos:
# La orientación a objetos es un paradigma de programación que proporciona unas estructuras 
# denominadas objetos con el objetivo de estructurar los programas para que propiedades y 
# comporatamientos similares se agrupen.

## **Python es un lenguaje orientado a objetos y todas las estructuras que hemos visto en secciones previas son objetos.**

# La programación orientada a objetos nos permite crear estruturas que representan cosas de la 
# vida real a través de una construcción de que se donomina `clase` y después crear objetos 
# basándonos en estas clases.

# ----------------------------------------------------


## Clases en Python
# Las clases son la estructura principal de la programación orientada a objetos y nos 
# proporcionan un medio para agrupar datos y funcionalidad. 

# **Al crear una nueva clase se crea un nuevo tipo de dato, lo que permite crear nuevas 
# instancias de ese tipo que se denominan objetos**. Cada instancia de clase puede 
# tener atributos adjuntos para mantener su estado. Las instancias de clase también 
# pueden tener métodos (definidos por su clase)  para modificar su estado.

# La sintaxis que se utiliza para definir clases en Python 3 es la siguiente:
# class <nombre_clase>:
#     <sentencia(s)>

class Demo:
    pass


# ----------------------------------------------------

## Objetos en Python
# Una vez que hemos definido una clase, podemos utilizarla para crear varios objetos 
# pertenecientes a esa clase. La creación de un nuevo objeto a partir de una clase se 
# denomina **instanciar**.

# La sintaxis que utilizamos en Python 3 para instanciar un objeto es: 
# <nombre_clase>([<argumentos>])

demo = Demo()

