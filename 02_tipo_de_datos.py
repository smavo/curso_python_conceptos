# En Python, hay varios tipos de datos que se utilizan para almacenar diferentes tipos de información. 

## Enteros (int): Representan números enteros, positivos o negativos, sin decimales. Por ejemplo: 
x,y,z = 5, -10, 1000 
print(z,x,y)


## Flotantes (float): Representan números con decimales. Por ejemplo: 
a,b,c = 3.14, -0.5, 2.0
print(a,b,c)


# Cadenas de texto (str): Se utilizan para almacenar texto. 
# Puedes definirlas usando comillas simples o dobles. Por ejemplo: 
message = "Hola, mundo"
print(message)


# Booleanos (bool): Representan valores de verdad, es decir, True (verdadero) o False (falso). 
# Se utilizan en expresiones lógicas y de control de flujo.
valor_1 = True
valor_2 = False

if valor_1 == False:
    print(f'El valor es {valor_1}')
else: 
    print(f'El valor es {valor_2}')


valores = f'El valor es {valor_1}' if valor_1 == True else f'El valor es {valor_2}'
print(valores)


# Listas: 
# Son colecciones ordenadas y modificables de elementos. 
# Los elementos pueden ser de diferentes tipos. Por ejemplo: 
number = [1, 2, 3]
fruits = ['manzana', 'banana', 'cereza']
print(number, fruits)


# Tuplas: 
# Son colecciones ordenadas e inmutables de elementos. 
# Una vez que se crean, no se pueden modificar. Por ejemplo:
num = (1, 2, 3)
print(num)


# Diccionarios: 
# Son colecciones desordenadas de pares clave-valor. 
# Se utilizan para mapear claves a valores. Por ejemplo:
tp =  {'nombre': 'Juan', 'edad': 30}
print(tp)


# Conjuntos (set): 
# Son colecciones desordenadas de elementos únicos. 
# Se utilizan para realizar operaciones matemáticas de conjunto. Por ejemplo: {1, 2, 3}.
cjtos = {1, 2, 3}


# NoneType: 
# Representa la ausencia de valor. 
# Especialmente útil para indicar que una variable no tiene un valor asignado.
ntp = None
print(ntp)


# Bytes y bytearray: Se utilizan para representar datos binarios. Son útiles para trabajar con archivos y protocolos de red.