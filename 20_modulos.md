
# Modulos

### 1.  ¿Qué es la programación modular?

# La programación modular se refiere al proceso de dividir una tarea de programación 
# grande y difícil de manejar en subtareas o módulos separados, más pequeños y manejables. 
# Los módulos individuales se irán uniendo posteriormente para crear un programa más grande.

# La modularización del código en una aplicación grande tiene varias ventajas:
# * **Simplicidad**: En lugar de centrarse en todo el problema, un módulo suele centrarse en una parte relativamente pequeña del problema. Si trabajas en un solo módulo, tendrás un dominio del problema más pequeño en el que centrarte. Esto hace que el desarrollo sea más fácil y menos propenso a errores.
# * **Mantenimiento**: Los módulos se diseñan normalmente de manera que imponen límites lógicos entre los diferentes dominios del problema. Si los módulos se escriben de forma que se minimice la interdependencia, se reduce la probabilidad de que las modificaciones en un solo módulo tengan un impacto en otras partes del programa.
# * **Reutilización**: La funcionalidad definida en un solo módulo puede ser fácilmente reutilizada (a través de una interfaz bien definida) por otras partes de la aplicación. Esto elimina la necesidad de duplicar el código.
# * **Alcance**: Los módulos suelen definen un namespace (namespace global) separado, lo que ayuda a evitar colisiones entre nombres en diferentes áreas de un programa.
# **Las funciones, las clases, los módulos y los paquetes son construcciones de Python que promueven la modularización del código.**


# ¿Qué es un Módulo?
# Hay tres formas diferentes de definir un módulo en Python:
# * Un módulo puede estar escrito en Python.
# * Un módulo puede estar escrito en C y cargado dinámicamente en tiempo de ejecución.
# * Un módulo puede estar incorporado por defecto en el intérprete.

# En los tres casos se accede al contenido de un módulo de la misma manera: con la sentencia `import`.

# El tipo de módulo más importante y utilizado un 99% de las veces es el escrito en Python, que será en el que nos centraremos en este tema.

# Un módulo escrito en Python no es más que un archivo que contiene código en Python y una extensión `.py`. Esto es todo. No se requiere ningún tipo de sintaxis especial para definirlos.

```
cadena_texto = "Hola mundo"
lista = ["azul", "verde", "rojo"]

def funcion(arg):
    print(arg)
    
class Coche:
    pass
```

# Resultado:
    print(mimodulo.cadena_texto)
    print(mimodulo.lista)
    mimodulo.funcion("Hola mundo")
    bmw = mimodulo.Coche()

# Cuando el intérprete ejecuta la sentencia `import`, busca el `mimodulo.py` en una lista de directorios que obtiene a partir de las siguientes fuentes:

* El directorio desde el que se ejecutó el script o el directorio actual si el intérprete se está ejecutando de forma interactiva
* La lista de directorios contenida en la variable de entorno `PYTHONPATH`, si está configurada.
* Una lista de directorios dependiente de la instalación configurada en el momento de instalar Python



# La ruta de búsqueda resultante es accesible en la variable de Python `sys.path`, que se obtiene de un módulo llamado sys:

```
import sys 
sys.path
```

Por lo tanto, para asegurarnos de que el módulo es encontrado, se requiere que hagamos alguna de las siguientes acciones:

* **Guardar el `módulo.py` en el directorio donde se encuentra el script o en el directorio actual si estamos utilizando el interprete interactivo**
* Modificar la variable de entorno `PYTHONPATH` para que contenga el directorio donde se encuentra el módulo, o bien, guardar el módulo en uno de los directorios ya contenidos en esta variable
* Guardar el módulo en uno de los directorios dependientes de la instalación, a los que puede o no tener acceso de escritura, dependiendo del sistema operativo