
# Diccionarios
"""
Un diccionario es un conjunto de parejas **clave- valor** (key-value). 
Es decir, se accede a cada elemento a partir de su clave. 
Se definen de la siguiente manera:
"""
estudiante = {
	"nombre": "Sergio Villagomez Ortega",
	"edad": 25,
	"nota_media": 5.25,
	"repetidor" : False
}

print(estudiante)


# Las **claves tienen que ser únicas** y estar formadas por un **string o un número**. 
# Para acceder al valor de una clave exiten dos maneras distintas:

# Acceder al valor de una clave
edad = estudiante["edad"] # devuelve el valor de 'edad'
print(edad)

nota_media = estudiante.get("nota_media") # devuelve el valor de 'nota_media'
print(nota_media)


# Insertar o actualizar un valor:
estudiante["edad"] = 25 # actualiza el valor de 'edad'
estudiante["suspensos"] = 3 # inserta una nueva pareja clave - valor
print(estudiante)


# insertar una pareja clave - valor o actualizar si ya existe:
estudiante.update({'aprobados':'8'})
print(estudiante)


# Algunos de los métodos más utilizados son los siguientes:
"""
| Método | Acción |
|--|--|
| `diccionario.keys()` | Devuelve todas las claves del diccionario |
| `diccionario.values()` | Devuelve todos los valores del diccionario |
| `diccionario.pop(clave[,<default>])` | Elimina la clave del diccionario y devuelve su valor asociado. Si no la encuentra y se indica un valor por defecto, devuelve el valor por defecto indicado. |
| `diccionario.clear()` | Vacía el diccionario |
| `clave in diccionario` | Devuelve True si el diccionario contiene la clave o False en caso contrario. |
| `valor in diccionario.values()` | Devuelve True si el diccionario contiene el valor o False en caso contrario. |
"""

## Recorrer un diccionario
# La forma más habitual de recorrer un diccionario es mediante 
# la sentencia `for`. Al recorrer un diccionario, por defecto se 
# iterará sobre sus claves:

diccionario1 =  {'a':1,  'b':2,  'c':3}
for key in diccionario1:
	print(key) # Resultado: a b c


# Es decir, el código anterior será equivalente al siguiente:

diccionario2 =  {1:'a',  2:'b',  3:'c', 4:'d'}
for key in diccionario2.keys():
	print(key) # Resultado: 1 2 3 4


# Por lo tanto, para iterar accediendo a los valores, 
# realizaremos lo siguiente:
diccionario3 =  {1:'Sergio',  2:'Daniel',  3:'Fernando', 4:'Raul'}
for key in diccionario3:
	print(diccionario3[key]) 
	# Resultado: 
		# Sergio 
		# Daniel 
		# Fernando 
		# Raul


# Otro manera alternativa sería empleando la función `items()`, 
# la cual devuelve el diccionario como tuplas de tipo (key,value):
diccionario4 =  {'a':1,  'b':2,  'c':3}
for key, value in diccionario4.items():
	print("El valor de %s is %d" % (key, value))
	# Resultado:
	# El valor de a is 1
	# El valor de b is 2
	# El valor de c is 3


## Borrar un elemento
# Para borrar un elemento de un diccionario se utiliza la instrucción `del`.
edades1 = {
   "Ane" : 22,
   "Jokin" : 27,
   "Aitor" : 15
}
del edades1["Aitor"]
print(edades1)


# Otra alternativa también utilizada y mencionada anteriormente es 
# la función `pop()`, el cual devuelve el valor del elemento eliminado:
edades2 = {
   "Ane" : 22,
   "Jokin" : 27,
   "Aitor" : 15
}
edades2.pop("Ane")
print(edades2)

# Un diccionario nunca debería contener dos claves iguales. 
# No obstante, en caso de contener una clave repetida, tanto `del` 
# como `pop()` eliminarán todas las claves coincidentes.