
# Diccionarios
"""
Un diccionario es un conjunto de parejas **clave- valor** (key-value). 
Es decir, se accede a cada elemento a partir de su clave. 
El valor de una clave puede ser un número, una cadena, o incluso otro diccionario.
Se definen de la siguiente manera:
"""
estudiante = {
	"nombre": "Sergio Villagomez Ortega",
	"edad": 14,
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


# ------- Actualizar pares clave-valor: -------
estudiante["edad"] = 25 # actualiza el valor de 'edad'
estudiante["suspensos"] = 3 # inserta una nueva pareja clave - valor
estudiante["Valor"] = True # Se esta agregando un nuevo par clave-valor
print(estudiante)


# Insertar un par clave-valor o actualizar si ya existe:
estudiante.update({'aprobados':'8'})
print(estudiante)


# Iniciar un diccionario vacio
frutas = {}

frutas['id'] = 1
frutas['nombre'] = 'Platano'
print(frutas)

frutas['id'] = 2
frutas['nombre'] = 'Piña'
print(frutas)



# Como accedemos a un valor dentro del diccionario
frutas2= {1:'Manzana', 2:'Fresa', 3:'Platano',}

fruta2 = frutas2[3].title()
print(f'La fruta seleccionada es {fruta2}')


# Usando get() para acceder a los valores de un diccionario
frutas3= {1:'Manzana', 2:'Mandarina', 3:'Fresa', 4:'Maracuya', 5:'Platano',6: 'Maracuya'}

get_fruta = frutas3.get(7, 'No tiene valor')
print(get_fruta)

get_fruta = frutas3.get(4)
print(get_fruta)


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
## Recorriendo todas las claves de un diccionario:
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



## Recorriendo todos los valores de un diccionario
# Por lo tanto, para iterar accediendo a los valores, 
# realizaremos lo siguiente:
diccionario3 =  {1:'Sergio',  2:'Daniel',  3:'Fernando', 4:'Raul'}
for valor in diccionario3:
	print(diccionario3[valor]) 
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


usuario_0 = { 'Sergio' : 'Python', 'Yadira' : 'Java', 'Fernando': 'PHP', 'Isela': 'PHP'}

for clave, valor in usuario_0.items():
	print(f'\nEl lenguaje favorito de {clave} es: {valor}')
# Resultado:
	# El lenguaje favorito de Sergio es: Python
	# El lenguaje favorito de Yadira es: Java
	# El lenguaje favorito de Fernando es: PHP


# Mostrar valores sin duplicados- Extrae solo los valores unicos
for usuario in set(usuario_0.values()):
	print(usuario.title())



# Recorriendo un diccionario en un orden particula:
frutas0= {3:'Manzana', 4:'Mandarina', 1:'Fresa', 2:'Maracuya', 5:'Platano',}
 
for id_, fruta in sorted(frutas0.items()):
	print(f'{id_} - {fruta}')


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