# OPERADORES
# Los operadores son símbolos especiales que se utilizan para realizar 
# operaciones en variables y valores. Los operadores se dividen en varias 
# categorías según el tipo de operación que realizan. 
# Aquí tienes algunos de los operadores más comunes en Python:

# Operadores aritméticos: 
# Se utilizan para realizar operaciones matemáticas básicas.
"""
+ (suma)
- (resta)
* (multiplicación)
/ (división)
% (módulo, devuelve el resto de la división)
** (exponente)
// (división entera)
"""
a = 10
b = 3

suma = a + b        # 10 + 3 = 13
resta = a - b       # 10 - 3 = 7
multiplicacion = a * b  # 10 * 3 = 30
division = a / b    # 10 / 3 = 3.333...
modulo = a % b      # 10 % 3 = 1 (resto de la división)
exponente = a ** b  # 10^3 = 1000
division_entera = a // b  # 10 // 3 = 3 (división entera, sin decimales)

print(f'la suma es: {suma}')
print(f'la resta es: {resta}')
print(f'la multiplicacion es: {multiplicacion}')
print(f'la division es: {division}')
print(f'el resultado del modulo es: {modulo}')
print(f'el resultado del exponente es: {exponente}')
print(f'la division entera es: {division_entera}')


# Operadores de asignación: 
# Se utilizan para asignar valores a variables.
"""
= (asignación simple)
+= (asignación con suma)
-= (asignación con resta)
*= (asignación con multiplicación)
/= (asignación con división)
"""
x = 8
print(x)

x += 2  # Ahora x es igual a 10
print(x)

x = 8
x -= 2  # Ahora x es igual a 6
print(x)

y = 8
y *= 2  # Ahora x es igual a 16
print(y)

z = 8
z /= 4  # Ahora x es igual a 2.0
print(z)



# Operadores de comparación: 
# Se utilizan para comparar valores y devuelven un valor booleano (True o False).
"""
== (igual a)
!= (diferente de)
< (menor que)
> (mayor que)
<= (menor o igual que)
>= (mayor o igual que)
"""

a = 5
b = 7

igual_a = a == b  # False, ya que 5 no es igual a 7
diferente_de = a != b  # True, ya que 5 es diferente de 7
menor_que = a < b  # True, ya que 5 es menor que 7
mayor_que = a > b  # False, ya que 5 no es mayor que 7
menor_o_igual = a <= b  # True, ya que 5 es menor o igual que 7
mayor_o_igual = a >= b  # False, ya que 5 no es mayor o igual que 7

print(igual_a)
print(diferente_de)
print(menor_que)
print(mayor_que)
print(menor_o_igual)
print(mayor_o_igual)



# Operadores lógicos: 
# Se utilizan para realizar operaciones lógicas en valores booleanos.
"""
and (y lógico)
or (o lógico)
not (negación lógica)
"""

x = True
y = False

y_logico = x and y  # False, ya que ambas condiciones deben ser True para que el resultado sea True
o_logico = x or y   # True, ya que al menos una de las condiciones es True
negacion = not x    # False, ya que negamos True y obtenemos False

print(y_logico)
print(o_logico)
print(negacion)



# Operadores de pertenencia: 
# Se utilizan para verificar si un valor está presente en una secuencia (como una lista o una cadena).
"""
in (está en)
not in (no está en)
"""
lista = [1, 2, 3, 4, 5]

esta_en_lista = 3 in lista  # True, ya que 3 está en la lista
no_esta_en_lista = 6 not in lista  # True, ya que 6 no está en la lista

print(esta_en_lista)
print(no_esta_en_lista)



# Operadores de identidad: Se 
# utilizan para verificar si dos objetos tienen la misma identidad 
# (es decir, si son el mismo objeto en la memoria).
"""
is (es)
is not (no es)
"""
a = [1, 2, 3]
b = a

es_el_mismo_objeto = a is b  # True, ya que a y b apuntan al mismo objeto en la memoria
no_es_el_mismo_objeto = a is not [1, 2, 3]  # True, ya que son dos objetos diferentes en la memoria

print(es_el_mismo_objeto)
print(no_es_el_mismo_objeto)

