
# Listas
# Es una colección de elementos en un orden particular. 
# Son colecciones ordenadas y modificables de elementos. 
# Los elementos pueden ser de diferentes tipos
autos = ['audi','lamborgini','mazda','nissan']
print(autos)


## Acceder a los elementos de la lista:
"""
Python considera que el primer elemento de una lista esta en la posición 0, no en la posición 1.
""" 
print(autos[0])  # .upper() = Mayuscula
print(autos[2]) # Accediendo al 3 elemento
print(autos[-1]) # Accediendo al ultimo elemento
print(autos[-2]) # Accediendo al penultimo elemento
print(autos[:2]) # Accediendo hasta la tercera posicion
print(autos[1:]) # Accediendo desde la segunda posicion hacia adelante


# Uso de valores individuales de la lista
print(f'La marca que me gusta mas es {autos[0].title()}')


# Modificación de elementos de una lista:
autos[-1] = 'toyota'
print(autos) 


# Agrear un elemento a la lista:
autos.append('Chevrolet')
autos.append('fiat')
print(autos)


# Insertar elementos en una lista:
autos.insert(1, 'Ferrari')
print(autos)


# Eliminar elementos de una lista:
del autos[-1]
print(autos)


# Eliminar un elemento usando el método pop(): 
# El método pop() Elimina el ultimo elemento de la lista
autos_list = autos.pop()
print(autos)
print(autos_list)
print(f"El ultimo elemento de la lista fue '{autos_list.title()}'")

autos_all = autos.pop(1) # Elimina el elemento en la posicion espeicificada
print(autos)
print(autos_all)
print(f"El elemento eliminado de la lista fue: '{autos_all.title()}'")


# Eliminar un elemento por valor: 
auto_remove = 'mazda'
autos.remove(auto_remove) 
print(autos)
print(f"El auto eliminado por el metodo remove es: '{auto_remove.title()}'")


# Organizar Listas:
motos = ['susuki','kawasaki','honda','pulsar']
motos.sort() # Ordena en orden alfabetico
print(motos) 

motos.sort(reverse=True) # Ordena en orden alfabetico inverso
print(motos)


motos_list1 = sorted(motos) # sorted devuelve la lista a su orden original
motos_list2 = sorted(motos, reverse=True) # Devuelve la lista en orden inverso
print(motos_list1)
print(motos_list2)


# Orden inverso
motos.reverse()
print(motos)


# Longitud en una Lista
frutas = ['manzana', 'pera', 'piña', 'fresa', 'naranja']
print(frutas)
print(len(frutas))


# Trabajando con el Bucle For en una lista
nombres = ['yadira', 'yanela', 'isela', 'aurea', 'graciela']
print(nombres)

for nombre in nombres:
    print(f'El nombre es: {nombre.title()}, y tiene  {len(nombre)} caracteres')


# Listas Numéricas
numero_listas = [ 1,2,3,4,5,6,7,8,9,0]
print(numero_listas)

for valor in range(1,6): # Tiene un rango de 0 al 5
    print(valor)

for val in range(2,9,2): # Comienza en el valor 2 y luego suma 2 a ese valor
    print(val)

for vall in range(0,9):
    print(vall**2) # calcula el exponente de un numero recorriendo el bucle For


# Estadistica simple con una lista de numeros
numero_listas1 = [ 1,2,3,4,5,6,7,8,9,10,11,12]

print(min(numero_listas1)) # Obtiene el numero minimo
print(max(numero_listas1)) # Obtiene el numero maximo
print(sum(numero_listas1)) # Obtiene la suma total de todos los numeros de la lista


# Lista de compresiones
calculos = [valores**2 for valores in range(0,11)]
print(calculos)