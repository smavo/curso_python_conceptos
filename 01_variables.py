
# Variables:
## Es un elemento de un lenguaje de programación que tiene asignado un valor determinado.

## Las variables en Python se pueden crear asignando un valor a un nombre sin necesidad de declararla antes.

x = 10
y = "Nombre"
z = 3.9


### Nombres de variables
### Podemos asignar el nombre que queramos, respetando no usar las palabras reservadas de Python ni espacios, guiones o números al principio.

# Válido
_variable = 10
vari_able = 20
variable10 = 30
variable = 60
variaBle = 10

print(_variable, vari_able, variable10, variable, variaBle)



##Los siguientes ejemplos no son permitidos.
# No válido
# 2variable = 10
# var-iable = 10
# var iable = 10

# Me devolvera el siguiente error: 
#  2variable = 10
#     ^
# SyntaxError: invalid decimal literal



## Asignar múltiples valores
### Se pueden asignar múltiples variables en la misma línea.
x, y, z = 10, 20, 30

## Imprimir variables
### Una variable puede ser impresa por pantalla usando print()

x = 10
y = "Nombre"

print(x)
print(y)


# ----------------------------
## Palabras reservadas en Python:
# Python tiene un conjunto de palabras reservadas que no podemos utilizar para nombrar variables ni funciones, ya que las reserva internamente para su funcionamiento.
# and
# assert
# break
# continue
# def
# elif
# else
# except
# exec
# finally
# for
# from 
# global
# if
# import
# in 
# is
# lambda
# not
# or 
# pass
# print
# raise
# return
# try
# while 


# ---------------------------------------
## Variables y alcance
#### Un concepto muy importante cuando definimos una variable, es saber el alcance o scope que tiene. 
# En el siguiente ejemplo la variable con valor 10 tiene un alcance global y la que tiene el 
# valor 5 dentro de la función, tiene un alcance local. Esto significa que cuando hacemos print(x), 
# estamos accediendo a la variable global n1 y no a la x definida dentro de la función.

n1 = 15

def funcion():
    n1 = 7
    return n1

result = funcion()

print(result)
print(n1)