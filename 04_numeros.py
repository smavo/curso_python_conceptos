
# Numeros

## Números enteros (int)
### 'Un entero es un múmero sin decimales, positivo o negativo.

"""
En Python el tamaño máximo que puede tener un entero depende de la
plataforma pero, como mínimo, será de 32 bits, lo que permite manejar un rango de
números entre el -2147483647 y el 2147483647. En ordenadores de 64 bits el rango
sube hasta -9223372036854775807 y 9223372036854775807.
"""
numero = 20 
print(numero)

operacion = 7 * 8
print(operacion)


# Números enteros largos (long)
"""
Si el entero no es suficiente disponemos del entero largo, cuya longitud es
arbitraria y no tiene límite superior ni inferior.

Para especificar que queremos que un número se almacene como tipo long y
no como tipo int le añadimos detrás una letra “L” de este modo:
"""

# Definir un número entero largo
numero_largo = 1234567890123456789012345678901234567890
resultado = numero_largo * 2
print(resultado)

# Otras formas de expresar numeros largos
number = 2e10
print(number)


number_2 = 14_000_000
print(number_2) 


# Números en coma flotante (float)
""""
Llamamos números en coma flotante a los números racionales. Es decir, a
los que tienen expansión decimal

El máximo número que permite este tipo es 1.7976931348623157e+308, y
el mínimo 2.2250738585072014e-308. En Python los decimales se separan con un
punto ().
"""
decimal_number = 10.5
print(decimal_number)


# ---------------------------------------------
# Convertir un String a Numero Entero 
numero1 = "32"
print(numero1)
print(int(numero1))

op = numero1 * 2
print(op)

opp = int(numero1) * 7
print(opp)


# Convertir un String a Numero Decimal
prueba1 = '17.5'
print(prueba1)
print(float(prueba1))

result = prueba1 * 2 
print(result)

result1 = float(prueba1) * 3
print(result1)

