## Cadenas de texto (string)
#  Las cadenas de texto o strings se definen mediante comilla simple (`' '`) o doble comilla (`" "`):
mi_nombre = 'Ane'
print(mi_nombre)
mi_nombre= "Ane"
print(mi_nombre)

# La diferencia principal se encuentra en que las comillas dobles aportan mayor facilidad en textos que incluyan apóstrofes:
mi_nombre = 'I\'m John'
print(mi_nombre)
mi_nombre= "I'm John"
print(mi_nombre)


#Para definir strings multi-línea se utiliza la triples comillas (`"""`):
frase = """ esto es una
        frase muy larga de más de
        una línea ... """
print(frase)


### Concatenación de strings
# Es posible unir dos strings con el operador `+`:
primera_palabra = 'Hola'
frase_completa = primera_palabra + ', mundo'
print(frase_completa)


segunda_palabra = 'mundo'
frase_completa = primera_palabra + ', ' + segunda_palabra
print(frase_completa)


### Método alternativo 1: str.join():
# El método `join()` recibe como argumento el listado (de tipo List, Tuple, String, Dictionary y Set) de strings que se desean concatenar. Se invoca sobre el separador que se utilizará para unir las cadenas (el cual a su vez es un string también):
strings = ['do', 're', 'mi']
separador = ' - '
separador.join(strings)

print(strings)
print(separador.join(strings))


## Para iterar un elemento detrás del otro se introducirá string vacío como separador:
strings = ['do', 're', 'mi']
''.join(strings)
print(''.join(strings))


### Método alternativo 2: `str.format()`:
# Python 3 introdujo una nueva forma para formatear strings, la cual sustituye a la anterior en la que se hace uso del operador `%`. Para ello se invoca el método `format()` de un string:
# Ordenado por defecto:
frase = "Meses: {}, {} y {}".format('Enero','Febrero','Marzo')
print(frase)

# Especificar el orden indicando la posición:
frase = "Meses: {1}, {0} y {2}".format('Enero','Febrero','Marzo')
print(frase)

# Especificar el orden mediante parejas clave-valor:
frase = "Meses: {ene}, {feb} y {mar}".format(ene='Enero', feb='Febrero',mar='Marzo')
print(frase)


### Cadenas 'f' (f-strings)
# La versión 3.6 de Python trajo un gran avance a la hora de integrar variables o expreiones en cadenas de carácteres. Se introdujeron las llamadas `f-strings`, una forma más cómoda y directa para insertar variables y expresiones en cadenas. Permiten introducir cualquier variable o expresión dentro de un string incluyendo la variable entre llaves `{` y `}`.
# Veamos un ejemplo:
nombre = "Nora"
edad = 22
saludo = f"Me llamo {nombre} y tengo {edad} años."
print(saludo)

## Para indicar que se trata de un `f-string`, este deberá incluir la letra 'f' antes del comiendo de la cadena (antes de las comillas). A continuación se muestra otro ejemplo en el que se introduce una expresión:
a = 4
b = 3
print(f"La multiplicación de {a} y {b} es igual a {a * b}")


### Conversión de tipos
# A la hora de concatenar un string con otras variables como `integer` o `float` puede haber problemas:
edad = 25
nota_media = 7.3
# print("Tengo " + edad + " años y mi nota media es " + nota_media + ".")

# Traceback (most recent call last):
#     File "<stdin>", line 1, in <module>
# TypeError: can only concatenate str (not "int") to str


# Mediante la función `str()` podemos convertir un valor a string y evitar así cualquier tipo de problema:
edad = 25
nota_media = 7.3
print("Tengo " + str(edad) + " años y mi nota media es " + str(nota_media) + ".")


# De igual manera es posible convertir a otros tipos con las funciones `int()`, `float()` and `bool()`.



### Métodos en cadenas de texto (string)
# Es posible **obtener un carácter concreto** de un string utilizando los corchetes `[]` y el índice del carácter al que queremos acceder:
frase = 'Aprendiendo a programar en Python'
frase[0] # devuelve el primer caracter
frase[1] # devuelve el segundo caracter
frase[-1] # devuelve el primer caracter empezando por el final
frase[-2] # # devuelve el segundo caracter empezando por el final
print(frase)
print(frase[0])
print(frase[1])
print(frase[-1])
print(frase[-2])


# Si queremos **obtener un substring**, utilizaremos la siguiente notación:
frase = 'Aprendiendo a programar en Python'
mi_substring = frase[1:5] 
# devuelverá los caracteres desde la posición 1 hasta la 5 (no incluye el 5)
print(mi_substring)

# En caso de dejar la primera variable vacía, se considera la primera posición del string. Dejando la segunda variable vacía se considera la última posición del string:
frase = 'Aprendiendo a programar en Python'
mi_substring = frase[:5]
print(mi_substring)

mi_substring = frase[4:]
print(mi_substring)



# Otros métodos útiles de string:
# len(str) # devuelve la longitud del string
# str.upper() # convierte a mayúsculas
# str.lower() # convierte a minúsculas
# str.title() # convierte a mayúsculas la primera letra de cada palabra
# str.count(substring [, inicio, fin]) # devuelve el número de veces que aparece
# # el substring en el string. Opcionalmente se puede indicar el inicio y fin. 
# str.find(‘d’) # devuelve el índice de la primera aparición de 'd'
# # (devolverá -1 si no lo encuentra)
# substr in str # devuelve True si el string contiene el substring
# str.replace(old, new [, count]) # reemplaza 'old' por 'new' un máximo de 'count' veces.
# str.isnumeric() # devuelve True si str contiene solamente números


# ----------------------------------------------------------------------------

# La indexación y el slicing (rebanado) son técnicas fundamentales en Python para acceder a elementos individuales o rangos de elementos en secuencias, como listas, tuplas y cadenas de texto. Aquí te proporcionaré una introducción a la indexación y el slicing en Python.

# Indexación en Python:

# La indexación se utiliza para acceder a elementos individuales en una secuencia (como una lista o una cadena) utilizando su posición o índice. Los índices en Python comienzan en 0, lo que significa que el primer elemento tiene un índice de 0, el segundo tiene un índice de 1, y así sucesivamente. Puedes acceder a un elemento utilizando el operador de corchetes [].
# Ejemplo de indexación en una lista:
mi_lista = [10, 20, 30, 40, 50]
primer_elemento = mi_lista[0]  # Accede al primer elemento (índice 0)
print(primer_elemento)  # Imprime 10


# Slicing (Rebanado) en Python:
# El slicing es una técnica que te permite extraer subconjuntos de elementos de una secuencia 
# utilizando rangos de índices. La sintaxis básica del slicing es secuencia[inicio:final],
# donde inicio es el índice del primer elemento que deseas incluir en el resultado, y final 
# es el índice del primer elemento que deseas excluir del resultado.

## Ejemplo de slicing en una lista:
mi_lista = [10, 20, 30, 40, 50]
sublista = mi_lista[1:4]  # Obtiene elementos desde el índice 1 hasta el índice 3 (no incluye el 4)
print(sublista)  # Imprime [20, 30, 40]
# También puedes omitir el valor de inicio o final en el slicing para indicar que deseas empezar 
# desde el principio o llegar hasta el final de la secuencia, respectivamente.


## Ejemplo de slicing sin especificar inicio o final:
mi_lista = [10, 20, 30, 40, 50]
primeros_tres = mi_lista[:3]  # Obtiene los primeros tres elementos (desde el principio hasta el índice 2)
ultimos_dos = mi_lista[3:]  # Obtiene los dos últimos elementos (desde el índice 3 hasta el final)
print(primeros_tres)  # Imprime [10, 20, 30]
print(ultimos_dos)  # Imprime [40, 50]
# Además, puedes utilizar índices negativos en el slicing para contar 
# desde el final de la secuencia.


# Ejemplo de slicing con índices negativos:
mi_lista = [10, 20, 30, 40, 50]
ultimos_tres = mi_lista[-3:]  # Obtiene los tres últimos elementos
print(ultimos_tres)  # Imprime [30, 40, 50]

# El slicing es una técnica poderosa que te permite trabajar con subconjuntos de datos 
# en Python de manera eficiente. Puedes aplicarlo a listas, tuplas, cadenas y otras secuencias.


# ----------------------------------------------------------------------------

# El término "stride" en Python generalmente se refiere a la "longitud del paso" o al número 
# de elementos que se saltan al recorrer una secuencia, como una lista o una cadena de texto, 
# durante la iteración o el acceso a elementos. Puedes usar el stride para acceder a elementos o 
# realizar operaciones en intervalos específicos en una secuencia.

# El stride se utiliza en combinación con la indexación y el slicing en Python. La sintaxis básica 
# es secuencia[inicio:final:paso], donde inicio es el índice del primer elemento que deseas incluir, 
# final es el índice del primer elemento que deseas excluir, y paso es la longitud del paso o el 
# número de elementos que se deben saltar en cada iteración.

# Aquí tienes algunos ejemplos para ilustrar cómo funciona el stride:
# Acceder a elementos con un stride:
mi_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
elementos_con_stride = mi_lista[::2]  # Obtiene cada segundo elemento desde el principio
print(elementos_con_stride)  # Imprime [0, 2, 4, 6, 8]

# Invertir una cadena con un stride:
cadena = "Python"
cadena_invertida = cadena[::-1]  # Invierte la cadena
print(cadena_invertida)  # Imprime "nohtyP"

# Iterar con un stride:
mi_lista = [0, 1, 2, 3, 4, 5]
for elemento in mi_lista[::2]:
    print(elemento)
# Imprime 0
# Imprime 2
# Imprime 4
# El stride es una técnica útil para procesar datos en secuencias de una manera más específica y controlada. Puedes ajustar el valor del stride según tus necesidades para acceder a elementos o realizar operaciones en intervalos específicos dentro de una secuencia.



### # Stripping (Eliminación de Espacios en Blanco):
# Stripping se refiere a la eliminación de espacios en blanco, como espacios en blanco al principio y 
# al final de una cadena de texto. En Python, puedes usar los métodos strip(), lstrip(), y rstrip() para 
# eliminar estos espacios en blanco.

# strip(): Elimina espacios en blanco al principio y al final de una cadena.
texto = "   Hola, mundo   "
texto_stripped = texto.strip()
print(texto_stripped)  # Imprime "Hola, mundo"

#lstrip(): Elimina espacios en blanco del lado izquierdo de una cadena.
texto = "   Hola, mundo   "
texto_lstripped = texto.lstrip()
print(texto_lstripped)  # Imprime "Hola, mundo   "

# rstrip(): Elimina espacios en blanco del lado derecho de una cadena.
texto = "   Hola, mundo   "
texto_rstripped = texto.rstrip()
print(texto_rstripped)  # Imprime "   Hola, mundo"

# Estas operaciones son útiles cuando necesitas manipular o limpiar datos en Python.


