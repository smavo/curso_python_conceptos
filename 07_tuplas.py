## Tuplas
"""
Las tuplas son **listas inmutables**. Es decir, una vez declaradas, 
no se pueden realizar modificaciones sobre ellas (añadir/eliminar elementos 
o hacer modificaciones sobre ellos). Para definir una tupla se escriben 
los elementos entre paréntesis:
"""
tamanios = (100, 50)
print(tamanios)

pi = (3.1416, )
print(pi)

for tamanio in tamanios:
    print(f'las medidas del rectangulo son: {tamanio}')

tamanios = (150, 70)
print(tamanios)


# tupla con valores mixtos
valores_mixtos = (1, "Hola", 2.5, False)
print(valores_mixtos)

# Acceder a los valores de una tupla
valores = ("a", "b", "c", "d", "e", "f")  
print(valores[1]) # Salida: 'b'
print(valores[2:4]) # Salida: ('c', 'd')
print(valores[3:])
print(valores[:4])


# Una acción típica de las tuplas es "desempaquetar" (unpack) sus valores, es decir, asignarlos a variables directamente:

tupla = (1, "Hola", 2.5) # Creamos la tupla
    
var1, var2, var3 = tupla # Hacemos el unpack

print(var1)      # 1
print(var2)      # 'Hola' 
print(var3)      # 2.5
