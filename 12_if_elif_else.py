### ---------- Sentencia IF - ELSE ----------
# Se evalúa la condición especificada en la sentencia `if` y en caso 
# de cumplirse se ejecutará el bloque de código indentado (tabulado). 
# En caso de que el resultado de la condición sea `False`, 
# el bloque especificado no se ejecutará:


# Igualdad
fruta = 'Manzana'

if fruta.lower() == 'manzana':
    print('la fruta es la correcta')
else:
    print('la fruta no es la correcta')


# Desigualdad
request_menu = 'tallarines'

if request_menu != 'causa':
    print('Es desigual')
else:
    print('Es el correcto')


# and | or
age1 = 10
age2 = 20

if (age1 >= 15) and (age2 <= 20):
    # print('la edad esta dentro del rango')
    print(True)
else:
    # print('la edad esta fuera del rango')
    print(False)


anio1 = 9

if (anio1 <= 10) or (anio1 >= 15):
    # print('la edad esta dentro del rango')
    print(True)
else:
    # print('la edad esta fuera del rango')
    print(False)



# Comprobar si un valor se encuentra [in] dentro de la lista
frutas1 = ['manzana', 'fresa', 'mango', 'papaya']
fruta1 = 'manzana'

if fruta1 in frutas1:
    print(f'la fruta {fruta1} esta en la lista')
else:
    print(f'la fruta {fruta1} no esta en la lista')


# Comprobar si el valor no se encuentra [is not] dentro de la lista
frutas2 = ['manzana', 'fresa', 'mango', 'papaya']
fruta2 = 'kiwi'

if fruta2 not in frutas2:
    print(f'la fruta {fruta2} no esta en la lista')
else:
    print(f'la fruta {fruta2} esta en la lista')


# if elif else
edad = 21

if (edad >=0) and (edad<=8):
    print(f'La persona es un niño y tiene {edad} años') 
elif (edad >=9) and (edad<=17):
    print(f'La persona es un adolescente y tiene {edad} años')  
elif (edad >=18) and (edad<=24):
    print(f'La persona es un joven y tiene {edad} años')  
else:
    print(f'La persona es un mayor de edad y tiene {edad} años')  



# uso de sentencias IF con listas
autos = ['audi', 'ferrari', 'toyota']

for auto in autos:
    if auto == 'bugati':
        print(f'el auto {auto} se encuentra seleccionado')
    else: 
        print(f'el auto {auto} no se encuentra seleccionado')



# Validaciones for + if
autos = ['audi', 'ferrari', 'toyota']

for auto in autos:
    if auto == "audi":
        print(auto.upper())
    else:
        print(auto.title())



# Trabajando con la consola 
message = input("Escribe tu Nombre: ")
edad = input('Cuantos años tienes?: ')
edad = int(edad)

print(f'Tu nombre es: {message}')

# if edad >= 18:
#     print(f'Usted tiene {edad} y puede realizar esta operacion')
# else:
#     print(f'Usted tiene {edad} y no puede realizar esta operacion')

resultado = (f'Usted tiene {edad} y puede realizar esta operacion') if edad >= 18 else (f'Usted tiene {edad} y no puede realizar esta operacion')
print(resultado)



entrada = input('Ingrese un número: ')
entrada = int(entrada)

# if entrada % 2 == 0:
#     print(f'El numero {entrada} es par.')
# else: 
#     print(f'El numero {entrada} es impar.')

rst = (f'El numero {entrada} es par.') if entrada % 2 == 0 else (f'El numero {entrada} es impar.')
print(rst)

