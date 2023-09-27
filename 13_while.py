### ---------- Sentencia WHILE ----------
# La sentencia `while` permite ejecutar un bloque de código mientras la 
# expresión que definamos se cumpla (es decir, devuelva `True`). 
# Python interpretará como `True` cualquier valor distinto a `0` o `None`.

entrada1 = input('Ingrese un numero de inicio: ')
entrada2 = input('Ingrese un numero de Fin: ')
entrada1 = int(entrada1)
entrada2 = int(entrada2)

while entrada1 <= entrada2:
    print(entrada1)
    entrada1 += 1 # entrada1 = entrada1 + 1



# Mensaje por consola - 'Salir'
prompt = '\nDime algo y lo imprimire'
prompt += "\nIngrese 'quit' para finalizar el programa: "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)



# Uso de 'break' : Se usa para salir del ciclo inmediatamente sin ejecutar ningun
# codigo restante en el ciclo, independientemente de los resultados de cualquier
# prueba condicional.
prompt = '\nEscribe el nombre de las cuidades que haz visitado: '
prompt += "\nIngrese 'quit' para finalizar el programa: "

while True:
    ciudad = input(prompt)
    
    if ciudad == 'quit':
        break
    else: 
        print(f'Si he ido a la cuidad de {ciudad.title()}')



# Uso de 'continue' : En lugar de salir de un bucle por completo sin ejecutar el 
# resto de su codigo, puede usar la instruccion 'continue' para volver al principio
# del bucle en funcion del resultado de una prueba condicional
numero_inicio = input('Ingrese un numero de inicio: ')
numero_final = input('Ingrese un numero de Fin: ')
numero_inicio = int(numero_inicio)
numero_final = int(numero_final)

while numero_inicio < numero_final:
    numero_inicio +=1

    if numero_inicio % 2 == 0:
        continue

    print(f'El numero impar es : {numero_inicio}')



# Usar Bucle While con Listas y Diccionarios
usuarios_no_confirmados = ['Sergio','Yadira','Fernando']
usuarios_confirmados = []

while usuarios_no_confirmados:
    usuario_actual = usuarios_no_confirmados.pop()

    print(f'Usuario Verificado: {usuario_actual.title()}')
    usuarios_confirmados.append(usuario_actual)
# Resultado:
    # Usuario Verificado: Fernando
    # Usuario Verificado: Yadira
    # Usuario Verificado: Sergio



# Eliminacion de todas las instancias de valores especificos 
mascotas = ['perro', 'gato', 'pescado dorado', 'gato', 'conejo', 'gato']
print(mascotas)

while 'gato' in mascotas:
    mascotas.remove('gato')

print(mascotas)
# Resultado: 
    # ['perro', 'pescado dorado', 'conejo']



# Llenar un diccionario con entrada de usuario
# Registro de encuestas de mascotas preferidas de los usuarios
responses = {}
sondeo_activo = True

while sondeo_activo:
    nombre = input('Podria ingresar su nombre: ')
    response = input('Cual es el nombre de tu mascota preferida? ')

    responses[nombre] = response
    
    repetir = input('Quieres continua - Responder (si/no) ')
    if repetir == 'no':
        sondeo_activo = False

print('Resultados: ')

for nombre, response in responses.items():
    print("El usuario " + nombre + " tiene como mascota a: " + response + ".")


# Algunos ejemplos adicionales
# Tabla de Multiplicar 
n_inicio = int(input('Ingrese el numero de inicio: ')) 
n_final = int(input('Ingrese el numero Final: ')) 
table = int(input('Ingrese la tabla que desea ver:'))

while n_inicio < n_final:
    rst1 = table * n_inicio
    print(f'El resultado de {table} * {n_inicio} = {rst1}')
    n_inicio += 1

