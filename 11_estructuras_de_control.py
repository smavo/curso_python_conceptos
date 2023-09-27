# Estructuras de control

## Condicionales
# Las estructuras de control se utilizan para **ejecutar bloques de código en función de condiciones**.

### ---------- Sentencia IF - ELSE ----------
# Se evalúa la condición especificada en la sentencia `if` y en caso 
# de cumplirse se ejecutará el bloque de código indentado (tabulado). 
# En caso de que el resultado de la condición sea `False`, 
# el bloque especificado no se ejecutará:
numero = 5
if numero > 1:
    # Se ejecutará cuando la condición sea True
    print("Es mayor que uno")

# Las condiciones pueden tener mayor complejidad:
edad = 16
altura = 175
if (edad > 14 and altura > 160):
    print("Puede montarse en la montaña rusa")


# Mediante la palabra reservada `else` es posible especificar un bloque 
# de código que se ejecute en caso de que la condición no se cumpla:
numero = 2
if numero > 10:
     # Se ejecutará cuando la condición sea True
    print("Es mayor que diez")
else:
    # Se ejecutará cuando la condición sera False
    print("Es menor o igual que diez")


# También podemos comprobar más condiciones mediante la expresión `elif`. 
# En este caso, se seguirán comprobando todas las condiciones `elif` 
# hasta que una de ellas se cumpla. En caso contrario, se ejecutará 
# el bloque de código dentro de `else` (si lo hubiera).
numero = 5

if numero < 3:
    print("Es menor que 3")
elif numero < 6:
    print("El número está entre el 3 y el 5")
else:
    print("Es mayor o igual a 6")


# Tal y como muestra el siguiente código de ejemplo, Python no tiene 
# limitaciones para anidar distintos bloques de `IF`s.
numero = 2

if numero >= 0:
    if numero == 0:
        print("El valor es 0")
    else:
        print("Es un número positivo")
else:
    print("Es un número negativo")



## ---------- Bucles ----------
# Los bucles permiten ejecutar un bloque de código tantas veces como 
# queramos. 

### ---------- Sentencia WHILE ----------
# La sentencia `while` permite ejecutar un bloque de código mientras la 
# expresión que definamos se cumpla (es decir, devuelva `True`). 
# Python interpretará como `True` cualquier valor distinto a `0` o `None`.
contador = 0
while(contador < 5):
    # Se ejecutará mientras la variable contador sea menor a 5.
    contador = contador+1
    print("Iteración número",contador)
print ("¡Fin!")


# Para detener una ejecución de forma voluntaria se utiliza la sentencia `break`:
contador = 0
while(contador < 5):
    contador = contador+1
    print("Iteración número",contador)
    if contador == 3:
        break
print ("¡Fin!")


# También es posible saltar únicamente la iteración actual mediante la 
# sentencia `continue`:
contador = 0
while(contador < 5):
    contador = contador+1
    if contador == 3:
        continue
    print("Iteración número {}".format(contador))
print ("¡Fin!")

# La salida del programa anterior será la siguiente:
    # Iteración número 1
    # Iteración número 2
    # Iteración número 4
    # Iteración número 5
    # Bucle while finalizado

# Otros lenguajes de programación ofrecen otra estructura similar conocida como `DO - WHILE`. No es el caso de Python, por lo que habría que emular dicho comportamiento mediante nuestro código.


#### Bucle WHILE con ELSE
# La expresión `else` puede utilizarse también tras un bloque `while`. 
# De este forma podemos definir un bloque de código que se ejecutará 
# una vez finalizado el bloque `while` (es decir, cuando la condición 
# se evalúe `False` y no se haya finalizado mediante un `break`):
count = 0

while(count < 5):
    count = count+1
    print("Iteración número {}".format(count))
else:
    print("Bucle while finalizado")
   


### ---------- Sentencia FOR ----------
# A diferencia de otros lenguajes de programación, en Python la sentencia 
# FOR itera únicamente por secuencias (listas, tuplas, cadenas de 
# caracteres,...).
alumnos = ["Ane", "Mikel", "Unai", "Lorea"]
for alumno in alumnos:
    print(alumno)


# También es posible utilizarlo para recorrer un string:
frase = "Aprendiendo Python"
for c in frase:
    print(c)


# Para detener una ejecución se utiliza la sentencia `break`:
numeros = [4,8,2,7,1,9,3,5]
total = 0

for n in numeros:
    total += n
    if total > 10:
        break


# Al igual que en otras estructuras de repetición, también es posible 
# saltar únicamente la iteración actual mediante la sentencia `continue`:
numeros = [4,8,2,7,1,9,3,5]
total = 0


# solo sumar los números impares
for num in numeros:
    if num % 2 == 0:
        print("Numero par, no lo sumamos")
        continue
    total += n



#### Bucle FOR con ELSE
# Python permite definir un bloque de código que se ejecutará una vez finalice la iteración por todos los elementos de una lista. Es importante mencionar que no se ejecutará si se ha finalizado mediante `break`.
alumnos = ["Ane", "Mikel", "Unai", "Lorea"]

for alumno in alumnos:
    print(alumno)
else:
    print("No quedan más alumnos.")



#### La función range()
# La función `range([start,]  stop  [,  step])` devuelve una secuencia de números. Es por ello que se utiliza de forma frecuente para iterar:
for i in range(3):
    print(i)
# 0
# 1
# 2



# También podemos indicar el inicio, fin y step:
# Itera un número específico de veces utilizando la función range().
print("Números del 5 al 10") 
for i in range(5,  10): 
    print(i,  end=', ')
# 5,  6,  7,  8,  9,


print("Números impares del 1 al 10")
for i in range(1,  10,  2):
    print(i,  end=', ')
# 1,  3,  5,  7,  9,



# Para iterar por una lista utilizando el índice, basta con combinarlo con la función `len()`:
    alumnos = ["Ane", "Mikel", "Unai", "Lorea"]
    for i in range(len(alumnos)):
    	print(alumnos[i])




# ------- Instrucción break: -------
# Se utiliza dentro de bucles (for o while) para salir del bucle 
# prematuramente si se cumple una condición.
numeros = [1, 2, 3, 4, 5, 6]

for numero in numeros:
    if numero == 4:
        print("Se encontró el número 4")
        break
    print(numero)



# ------- Instrucción continue: -------
# Se utiliza dentro de bucles para saltar la iteración actual y continuar 
# con la siguiente si se cumple una condición.
for i in range(1, 6):
    if i == 3:
        print("Saltando el número 3")
        continue
    print(f"Número: {i}")



# ------- Estructura de control try-except: -------
# Permite manejar excepciones o errores en Python. Puedes capturar 
# y gestionar errores específicos.
try:
    resultado = 10 / 0  # Esto generará una excepción de división por cero
except ZeroDivisionError:
    print("Error: No se puede dividir por cero")
except Exception as e:
    print(f"Ocurrió una excepción: {e}")
else:
    print("La operación se realizó con éxito")
finally:
    print("Este bloque siempre se ejecuta")