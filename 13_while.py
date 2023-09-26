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
prompt += "\nIngrese 'salir' para finalizar el programa: "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

