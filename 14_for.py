
### ---------- Sentencia FOR ----------
# A diferencia de otros lenguajes de programación, en Python la sentencia 
# FOR itera únicamente por secuencias (listas, tuplas, cadenas de 
# caracteres,...).
nombres_apellidos = [("Alice", "Johnson"), ("Bob", "Smith"), ("Charlie", "Brown")]

for nombre, apellido in nombres_apellidos:
    nombre_completo = f"{nombre} {apellido}"
    print(nombre_completo)


productos = {
    "manzanas": 1.99,
    "plátanos": 0.99,
    "naranjas": 2.49,
    "uvas": 3.99
}

for producto, precio in productos.items():
    print(f"{producto}: ${precio}")


# También es posible utilizarlo para recorrer un string:
texto1 = "Hola, mundo!"

for caracter in texto1:
    print(caracter)



texto = "Python es un lenguaje de programación versátil y poderoso"
vocales = "aeiouAEIOU"

contador_vocales = 0

for caracter in texto:
    if caracter in vocales:
        contador_vocales += 1

print("Número de vocales en el texto:", contador_vocales)



texto2 = "Python es un lenguaje de programación versátil y poderoso"

palabra_buscada = "programación"

if palabra_buscada in texto2:
    print(f"{palabra_buscada} encontrada en el texto.")
else:
    print(f"{palabra_buscada} no encontrada en el texto.")



frase = "Los gatos son adorables"

nueva_frase = ""

for caracter in frase:
    if caracter == "a":
        nueva_frase += "o"
    else:
        nueva_frase += caracter

print("Frase original:", frase)
print("Frase modificada:", nueva_frase)



texto = "Python es un lenguaje de programación versátil y poderoso"

palabras = texto.split()
cantidad_palabras = len(palabras)

print("Cantidad de palabras en el texto:", cantidad_palabras)



# En este ejemplo, trabajamos con fechas y calculamos cuántos días 
# faltan hasta cada fecha en una lista.
from datetime import datetime

fechas = ["2028-09-30", "2026-10-05", "2024-10-10", "2023-10-15"]
hoy = datetime.today()

for fecha in fechas:
    fecha_objeto = datetime.strptime(fecha, "%Y-%m-%d")
    dias_hasta = (fecha_objeto - hoy).days
    print(f"Faltan {dias_hasta} días para {fecha}")


# Para detener una ejecución se utiliza la sentencia `break`:
numeros11 = [4,8,2,7,1,9,3,5]
total = 0

for n in numeros11:
    total += n
    if total > 10:
        break



# Ver solo numero pares
numeros22 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros_pares = []
for numero in numeros22:
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Números pares:", numeros_pares)



productos = {
    "manzanas": 1.99,
    "plátanos": 0.99,
    "naranjas": 2.49,
    "uvas": 3.99
}

for producto, precio in productos.items():
    print(f"{producto}: ${precio}")



#### Bucle FOR con ELSE
# Python permite definir un bloque de código que se ejecutará una vez finalice la iteración por todos los elementos de una lista. Es importante mencionar que no se ejecutará si se ha finalizado mediante `break`.
nombres = ["Alice", "Bob", "Charlie", "David"]
nombre_buscado = "Charlie"

for nombre in nombres:
    if nombre == nombre_buscado:
        print(f"{nombre_buscado} se encuentra en la lista.")
        break
else:
    print(f"{nombre_buscado} no se encuentra en la lista.")



contraseñas = ["clave123", "password456", "secreto789", "12345678"]

contraseña_valida = "secreto789"

for contraseña in contraseñas:
    if contraseña == contraseña_valida:
        print(f"Contraseña válida encontrada = {contraseña}")
        break
else:
    print("Ninguna contraseña válida encontrada.")



#### La función range()
# La función `range([start,]  stop  [,  step])` devuelve una secuencia de números. Es por ello que se utiliza de forma frecuente para iterar:

# Generar una secuencia de números del 2 al 8 (start=2, stop=9, step=1):
for i in range(1, 9):
    print(i)


# Generar una secuencia de números pares del 2 al 10 (start=2, stop=11, step=2):
for numero in range(2, 11, 2):
    print(numero)

# Iterar a través de una secuencia inversa:
for numero in range(10, 0, -1):
    print(numero)


# Dias habiles de un mes 
dias_habiles = 0

for dia in range(1, 31):
    if dia % 7 == 0:
        continue  # Saltar los fines de semana (sábados y domingos)
    dias_habiles += 1

print(f"El mes tiene {dias_habiles} días hábiles.")



# Numero de Habitaciones disponibles
habitaciones_disponibles = 0

for piso in range(1, 6):
    for habitacion in range(1, 11):
        # Simulando la verificación de disponibilidad
        if habitacion % 2 == 0:
            continue  # Saltar habitaciones ocupadas
        habitaciones_disponibles += 1

print(f"El hotel tiene {habitaciones_disponibles} habitaciones disponibles.")


# Calendario de 30 dias 
mes = "Septiembre"
dias_del_mes = 30

print(f"Calendario para {mes}:\n")

for dia in range(1, dias_del_mes + 1):
    print(f"{mes} {dia}")




# Para iterar por una lista utilizando el índice, basta con combinarlo con la función `len()`:
alumnos = ["Ane", "Mikel", "Unai", "Lorea"]
for i in range(len(alumnos)):
    print(f'El alumno {i} {alumnos[i]}')



# Encontrar el elemento máximo en una lista
valores = [15, 42, 7, 99, 23, 56]
maximo = valores[0]

for i in range(1, len(valores)):
    if valores[i] > maximo:
        maximo = valores[i]

print("El valor máximo en la lista es:", maximo)



# Generar una lista de cuadrados de números
numeros = [1, 2, 3, 4, 5]
cuadrados = []

for i in range(len(numeros)):
    cuadrado = numeros[i] ** 2
    cuadrados.append(cuadrado)

print("Cuadrados de los números:", cuadrados)



# Eliminar elementos duplicados de una lista:
numeros = [1, 2, 2, 3, 4, 4, 4, 5, 5, 7, 8, 0, 9, 10, 2, 4, 5]
sin_duplicados = []

for i in range(len(numeros)):
    if numeros[i] not in sin_duplicados:
        sin_duplicados.append(numeros[i])

print("Lista sin duplicados:", sin_duplicados)




# ------- Instrucción break: -------
# Se utiliza dentro de bucles (for o while) para salir del bucle 
# prematuramente si se cumple una condición.

# Mumero encontrado = 5
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_objetivo = 5

for numero in numeros:
    if numero == numero_objetivo:
        print(f"Se encontró el número {numero_objetivo}.")
        break


# Encontrar el nombre seleccionado
nombres = ["Alice", "Bob", "Charlie", "David", "Eva"]
nombre_buscado = "Charlie"

for nombre in nombres:
    if nombre == nombre_buscado:
        print(f"{nombre_buscado} se encuentra en la lista.")
        break
else:
    print(f"{nombre_buscado} no se encuentra en la lista.")



# Numeros pares encontrados 
numeros = [3, 7, 1, 4, 9, 6, 8]

for numero in numeros:
    if numero % 2 == 0:
        print(f"El primer número par encontrado es {numero}.")
        break


# Encontrar fruta seleccionada
diccionario = {"manzanas": 10, "plátanos": 5, "naranjas": 8}
cantidad_objetivo = 5

for fruta, cantidad in diccionario.items():
    if cantidad == cantidad_objetivo:
        print(f"La fruta con {cantidad_objetivo} unidades es: {fruta}")
        break



# ------- Instrucción continue: -------
# Se utiliza dentro de bucles para saltar la iteración actual y continuar 
# con la siguiente si se cumple una condición.

# Numeros Impares
for numero in range(1, 11):
    if numero % 2 == 0:
        continue  # Salta los números pares
    print(numero)


# Numeros Pares 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares = []

for numero in numeros:
    if numero % 2 != 0:
        continue  # Salta los números impares
    numeros_pares.append(numero)

print("Números pares:", numeros_pares)


# Cadena de Texto
texto = "Hola Mundo"

for caracter in texto:
    if caracter == ' ':
        continue  # Salta los espacios en blanco
    print(caracter)



# Numeros divisibles * 5 
numeros = [12, 9, 15, 23, 10, 7]

for numero in numeros:
    if numero % 5 != 0:
        continue  # Salta los números que no son divisibles por 5
    print(f"El primer número divisible por 5 es: {numero}")
    break  # Termina el bucle después de encontrar el primer número



# ------- Estructura de control try-except: -------
# Permite manejar excepciones o errores en Python. Puedes capturar 
# y gestionar errores específicos.
numeros = [1, 2, 3, 4, 5, "seis", 7, 8, "nueve", 10]

for elemento in numeros:
    try:
        # Intenta convertir el elemento a un entero y luego imprímelo
        numero = int(elemento)
        print(f"Elemento convertido a número: {numero}")
    except ValueError:
        # Si ocurre una excepción de tipo ValueError, muestra un mensaje de error
        print(f"Error: No se pudo convertir {elemento} a número")

# La ejecución continúa después del manejo de excepciones
print("Fin del bucle")



# Ejercicio tabla de multiplicar 
# Pedir al usuario el número de inicio, número final y la tabla de multiplicar
inicio = int(input("Ingrese el número de inicio: "))
final = int(input("Ingrese el número final: "))
tabla = int(input("Ingrese la tabla de multiplicar: "))

# Imprimir la tabla de multiplicar personalizada
print(f"Tabla de multiplicar del {tabla} desde {inicio} hasta {final}:")
for i in range(inicio, final + 1):
    resultado = tabla * i
    print(f"{tabla} x {i} = {resultado}")

