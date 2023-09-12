
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


