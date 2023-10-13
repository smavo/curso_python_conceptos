
# SCOPE 
### En Python, el alcance de una variable se refiere a la región en un programa en la que la variable es accesible y puede ser referenciada. 
### Python utiliza reglas específicas para determinar el alcance de una variable. Hay tres tipos de alcance en Python:

## Scope Local (local): Se refiere a variables definidas dentro de una función. Estas variables solo son accesibles desde esa función.
def my_function():
    x = 10  # Variable local
    print(x)

my_function()


## Scope Global (global): Se refiere a variables definidas fuera de cualquier función o en un alcance global. Estas variables son accesibles desde cualquier lugar en el programa.
x = 10  # Variable global

def my_function():
    print(x)

my_function()


## Scope no local (nonlocal): Se refiere a variables definidas en el ámbito de una función anidada y que no son globales. Si una variable no es ni local ni global, se asume que es una variable no local.
def outer_function():
    x = "local"

    def inner_function():
        nonlocal x
        x = "nonlocal"
        print("Inner:", x)

    inner_function()
    print("Outer:", x)

outer_function()

##Python sigue un conjunto específico de reglas para determinar el alcance de las variables. 
##Cuando se realiza una referencia a una variable, Python buscará primero en el ámbito local, 
##luego en el ámbito no local y finalmente en el ámbito global. 

##Si no se encuentra en ninguno de los ámbitos anteriores, se lanzará un error. 
##Para modificar una variable global dentro de una función, se debe usar la palabra clave global.

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Para modificar variables en diferentes ámbitos en Python, puedes utilizar las palabras clave global y 
# nonlocal según corresponda al ámbito que estés manipulando.

#### Para modificar una variable global dentro de una función:
x = 10  # Variable global

def modify_global():
    global x
    x = 20  # Modificar la variable global
    print("Dentro de la función:", x)

modify_global()
print("Fuera de la función:", x)


### Para modificar una variable no local (en una función anidada):
def outer_function():
    x = "local"

    def inner_function():
        nonlocal x
        x = "nonlocal"
        print("Dentro de la función interna:", x)

    inner_function()
    print("Dentro de la función externa:", x)

outer_function()


### Para modificar una variable local, no es necesario usar ninguna palabra clave especial, 
### simplemente asigna un nuevo valor a la variable local dentro de la función.
def modify_local():
    y = 10  # Variable local
    y = 20  # Modificar la variable local
    print("Dentro de la función:", y)

modify_local()


### Asegúrate de comprender el impacto de modificar variables en diferentes ámbitos, 
# ya que una gestión incorrecta puede llevar a resultados inesperados y errores en el código.