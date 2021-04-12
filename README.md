# Curso de Python intermedio

## Preparación antes de empezar

### Bienvenida al curso

### El Zen de Python

Son los 19 principios que tiene este lenguaje de programación poder escribir de manera precisa.

Para usar Python, en la CMD de Windows debemos escribir `py` , pero en un entorno tipo Linux, es `python3`

Para ver el zen de python usamos `import this`. This es un módulo oculto y secreto.

1. Bello es mejor que feo -> Python tiene la sintaxís más simple.
2. Explícito es mejor que implícito -> Siempre que podamos expresarnos en código para que el mismo se entienda mejor, vamos a hacerlo así.
3. Simple es mejor que complejo -> Si podemos resolver un problema en menos líneas de código y se entiende mejor, vamos por ese camino.
4. Complejo es mejor que complicado -> Si es necesario hacer las cosas complejas pero bien hechas, es mejor ese camino.
5. Plano es mejor que anidado -> Si tenemos muchos bloques de código, uno dentro de otro, la indentación será muy grande, esto lo debemos evitar.
6. Espaciado es mejor que denso -> Python nos obliga a hacer esto.
7. La legibilidad es importante -> Si podemos escribir código que se entienda mejor y que otras personas lo puedan entender, vamos por el buen camino.
8. Los casos especiales no son lo suficientemente especiales para romper las reglas -> Siempre que podamos respetar las reglas de Python, es mejor que lo hagamos así.
9. Sin embargo la practicidad le gana a la pureza -> Hay que tener un equilibro entre esta regla y la #8.
10. Los errores nunca deberían pasar silenciosamente -> Todo programador debe saber manejar errores
11. A menos que se silencien explícitamente -> Podemos hacer que los errores se silencien pero con consciencia.
12. Frente a la ambigüedad, evitar la tentación de adivinar -> Nuestro código debe tener solamente 1 interpretación.
13. Debería haber una, y preferiblemente solo una, manera obvia de hacerlo.
14. a pesar de que esa manera no sea obvia a menos que seas holandés (chiste del creador).
15. Ahora es mejor que nunca -> Si encontramos la solución hoy, no la dejes para mañana.
16. A pesar de que nunca es muchas veces mejorq que *ahora* mismo -> Si tenemos prisa, podemos hacer un mal código, es mejor dejarlo para después.
17. Si la implementación es difícil de explicar, es una mala idea. -> Si no podemos explicar nuestra idea, ni siquiera nostros mismos la entendemos.
18. Si la implementación es fácil de explicar, puede que sea una buena idea.
19. Los espacios de nombres son una gran idea, ¡tengamos más de esos! -> Tema avanzado de Python

### ¿Qué es la documentación?

La documentación es toda la información que nos explica cómo funciona un lenguaje de programación y/o una tecnología.

[Documentación oficial de Python](docs.python.org/es/3/)

PEP (Python Enhancement Proposals) son los documentos que conforman a toda la guía de estilos del lenguaje. Nos dicen cómo el lenguaje funciona y cómo deberíamos escribirlo.

[PEP 8](https://www.python.org/dev/peps/pep-0008/) recomendado por Facundo Martoni. Son las buenas prácticas.

## Entorno virtual

### ¿Qué es un entorno virtual?

Módulo -> Código escrito por otra persona que podemos usar nostros para resolver un problema de manera rápida. Por ejemplo, el módulo de números aleatorios.

En un entorno virtual tendremos diferentes proyectos, cada uno con una versión específica de Python y solamente funcionará para ese proyecto en particular.

### El primer paso profesional: creación de un entorno virtual

`python3.9 -m venv 'nombre_del_proyecto'`

-m es una bandera que significa "module".

venv significa "virtual enviroment".

Lo más común es que el nombre del proyecto sea "venv".

Si estás en linux y tienes el error:

"The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt-get install python3-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment."

Simplemente escribe: `sudo apt-get install python3.9-venv` (3.9 porque es la versión más actualizada)

Luego ejecuta `sudo python3.9 -m venv venv` y ya debería funcionar correctamente.

Para ejecutar el entorno virtual, justamente tenemos la ayuda del archivo "activate" dentro de la carpeta venv.

"This file must be used with "source bin/activate" *from bash* you cannot run it directly"

En mi caso en particual es `source venv/bin/activate`

Cuando tengamos venv activado vamos a estar usando el python que solamente funciona en el proyecto, no el global.

Para desactivar el entorno virtual solamente escribes `deactivate`.

Crear alias en linux: `alias avenv="source venv/bin/activate"`

### Instalación de dependencias con pip

PIP -> Package Installer for Python. Es el manejador de dependencias más popular de Python, porque viene de fábrica.

Algunos módulos populares son:

- Requests -> Web Scrapping
- BeautifulSoup4 -> Web Scrapping
- Pandas -> Data Science
- Numpy -> Data Science
- Pytest -> Testing

Antes de ponernos a descargar módulos, debemos primero activar el entorno virtual. Una vez hecho esto, usamos pip, la ventaja es que sólo se instalarán para el proyecto, no para toda la computadora.

`pip freeze` nos dará un listado de todos los módulos que tenemos instalados.

Podemos pensar en pip como el npm de Python. `pip install pandas`

Si estamos en Linux, y al tratar de instalar un módulo tenemos el error "Errno 13" y tampoco funciona la sugerencia de `--user`, debemos hacer esto: entrar al archivo pyvenv.cfg
Hacer esta modificación: `include-system-site-packages = true`
Apagas el entorno virtual, lo vuelves a encender y ya podrás descargar módulos en tu proyecto de Python.

Para que otra persona pueda trabajar en este proyecto, debe tener la misma versión de Python y las mismas dependencias. Para esto, haremos `pip freeze > requirements.txt`. Así, la persona que quiere trabajar con nosotros solamente hará `pip install -r requirements.txt` y listo.

Es buena práctica ignorar la carpeta venv, es como el node_modules de js.

### Una alternativa: Anaconda

Anaconda es un software completo pensado para los cientificos de datos. Nos permite crear un entorno virtual e instalar dependencias pero de manera gráfica.

[Página de Anaconda](https://www.anaconda.com/products/individual)

[Documentación oficial de Anaconda](https://docs.anaconda.com/)

[Instalar un GUI para WSL](https://www.youtube.com/watch?v=IL7Jd9rjgrM)

Para abrir anaconda en Linux usamos `anaconda-navigator`

#### Quiz

- Si actualizamos algún módulo de Python dentro de nuestro entorno virtual ¿esto afecta a otras versiones del mismo módulo dentro de nuestro computador?: NO
- ¿Con qué comando se activa un entorno virtual en Windows?: .\venv\Scripts\activate
- Selecciona el comando para instalar requests: pip install requests

## Alternativa a los ciclos: comprehensions

### Listas y diccionarios anidados

Es buena práctica ignorar la carpeta del entorno virtual en .gitignore.

### List comprehensions

`squares = [i**2 for i in range(1,101) if i % 3 != 0]` -> [element for element in iterable if condition]

- element -> Representa a cada uno de los elementos a poner en la nueva lista
- for element in iterable -> Ciclo a partir del cual se extraerán elementos de otra lista o cualquier iterable
- if condition -> Condición opcional para filtrar los elementos del ciclo

### Dictionary comprehensions

`cubes = {i:i**3 for i in range(1,101) if i % 3 != 0}`-> {key:value for value in iterable if condition}

- key:value -> Representa a cada una de las lalves y valores a poner en el nuevo diccionario
- for value in iterable -> Ciclo a partir del cual se extraerán elementos de cualquier iterable
- if condition -> Condición opcional para filtrar los elementos del ciclo

### Quiz 2

- ¿Puede un diccionario contener listas?: verdadero
- En un list comprehension el ciclo es: Obligatorio
- En un dictionary comprehension la condición es: opcional

## Conceptos avanzados de funciones

### Funciones anónimas: lamba

Son funciones sin nombre. `lamba argumentos:expresión`

Lambda solamente puede tener 1 expresión.

```python
palindrome = lambda string: string == string[::-1] #Variable stores the function value

print(palindrome('ana')) # returns True
```

El código de arriba es equivalente a:

```python
    def palindrome(string):
        return string == string[::-1]

    print(palindrome('ana'))
```

### High order functions: filter, map y reduce

Una función de orden superior es una función que recibe como parámetro a otra función

```python
def saludo(func):
    func()


def hola():
    print('hola!')


def adios():
    print('adios!')


saludo(hola) # prints hola!
saludo(adios) #prints adios!
```

Tenemos 3 funciones de orden superior que son muy importantes en lenguaje de programación:

- Filter
- Map
- Reduce

#### Filter

```python
my_list = [1,4,5,6,9,13,19,21]

odd = [i for i in my_list if i % 2 != 0]

print(odd) # prints [1,5,9,13,19,21]
```

Esto es list comprehension. Ahora con Filter:

```python
my_list = [1,4,5,6,9,13,19,21]

odd = list(filter(lamba x: x % 2 != 0 , my_list)) # second parameter of filter is an iterator

print(odd) #prints [1,5,9,13,19,21]
```

#### Map

```python
my_list = [1,2,3,4,5]
print([i**2 for i in my_list]) #prints [1,4,9,16,25]
```

Esto es con list comprehension. Ahora usemos map:

```python
my_list = [1,2,3,4,5]

squares = list(map(lmabda x: x**2, my_list))

print(squares) #prints [1,4,9,16,25]
```

#### Reduce

```python
from functools import reduce

my_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a * b , my_list)

print(all_multiplied) #prints 32
```

### Proyecto: filtrando datos

`old_people = list(map(lambda worker: worker | {"old": worker["age" > 70]} , DATA))` En Python 3.9 el pipe | sirve para sumar diccionarios.

### Quiz 3

- ¿Cuántos argumentos como máximo puede contener una función anónima?: infinitos
- ¿Cuál de las siguientes opciones **NO** es una función de orden superior?: open
- ¿Qué devuelve la función reduce?: Un elemento único

## Manejo de errores

### Los errores en el código

Errores:

- Syntax Error -> Errores de escritura, Python no ejecuta el programa.
- Exception -> Python se detiene en una línea en específica
  - KeyboardInterrupt -> Ctrl + C
  - KeyError -> Cuando tratamos de acceder a una llave que no existe
  - IndexError -> Cuando tratamos de acceder a un índice que no existe
  - FileNotFoundError -> Archivo que no existe
  - ZeroDivisionError -> Dividir entre 0
  - ImportError -> Intentamos importar un módulo que tiene un error

Estos son solo algunos ejemplos, hay más de 50 excepciones.

"Elevar", quiere decir que Python crea un objeto de tipo excepción.

**Traceback** son los errores que muestran en las consolas. Lo correcto es leer desde el final hasta el principio. En el final nos dirá cuál es la excepción que ocurrió.

### Debugging

O depuración, en español.

Al hacer debugging tenemos los botones de:

- Pausa -> Detiene el programa
- Paso siguiente -> Vamos a la siguiente línea de código
- Meternos -> Nos vamos a meter a la función de la línea del código, vamos a tener más detalles de lo que está pasando
- Salir -> Salimos de la línea de código
- Reiniciar -> Reiniciamos el programa
- Detener -> Salimos de la depuración

### Manejo de excepciones

```python
try:
    pass #Código a evaluar
except:
    pass #Si ocurre un error, llegará a esta parte
```

Ejemplo con try, raise, except:

```python
def palindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se pueden ingresar cadenas vacías")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False


try:
    print(palindrome(""))
except TypeError:
    print("Solo se pueden ingresar strings")
```

finally no es muy usado pero aún así es necesario mencionarlo. Corresponde al final de un bloque try. Se usa en casos muy particulares, por ejemplo; cerrar un archivo, cerrar una conexión a una base de datos o liberar recursos externos.

```python
try:
    f = open("archivo.txt")
    # hacer cualquier cosa con nuestro archivo
finally:
    f.close()
```

Algo que aparece casi al final de la lectura recomendada en el documentación de Python es que se puede agregar un “else” al try-except.

- TRY: En el try se coloca código que esperamos que pueda lanzar algún error.
- EXCEPT: En el except se maneja el error, es decir, si ocurre un error dentro del bloque de código del try, se deja de ejecutar el código del try y se ejecuta lo que se haya definido en el Except.
- ELSE: El else se ejecuta sólo si no hubo ninguna excepción lanzada desde el try
- FINALLY: Se ejecuta SIEMPRE, haya sido lanzada la excepción o no haya sido lanzada.

```python
try:
    pass
except Exception:
    print('Ocurrió una excepción')
else:
    print('No ocurrió ninguna excepción')
finally:
    print('Siempre me ejecuto')
```

### Poniendo a prueba el manejo de excepciones

### Assert statements

Son expresiones. Serían algo como: Código -> Assert statement y puede salir código o error.

`assert condición , mensaje de error` y se lee: "Afirmo que esta condición es verdadera, si no, imprimo este mensaje de error.

```python
def palindrome(string):
    assert len(string) > 0, "No se pueden ingresar cadenas vacías"
    return string == string[::-1]


print(palindrome("")) # print 'AssertError: No se pueden ingresar cadenas vacías'
```

Existe un método en Python llamado `isnumeric()` que funciona justamente con los strings.

### Quiz 4

- ¿Cuál de las siguientes opciones es una excepción válida?: ValueError
- ¿Cuál es la estructura correcta de un assert statement?: assert condición, mensaje
- ¿Cuál es la excepción que simboliza que intentamos acceder a un índice inexistente en una lista?: IndexError

## Manejo de archivos

### ¿Cómo trabajar con archivos?

Tenemos 2 clases de archivos:

- de texto -> tienen bytes por dentro que representan números y letras.
- binarios -> tienen bytes que son cosas mucho más complejas.

Con la programación en general no vamos a interactuar con los archivos binarios, pero sí con los de texto. Particularmente en el Backend se usa mucho el archivo `.json`. Mientras tanto en Ciencia de Datos se usa mucho `.csv`.

Modos de apertura:

- r -> Lectura (Read).
- r+ -> Lectura y escritura.
- w -> Escritura (Write) (sobreescribir).
- w+ -> Escritura y lectura. Sobre escribe el archivo si existe. Crea el archivo si no existe.
- a -> Escritura (Append) (agregar al final).
- a+ -> Añadido (agregar contenido) y lectura. Crea el archivo si éste no existe.

`with open("./ruta/del/archivo.txt" , "r") as f` -> with es un manejador contextual. Ayuda a que, en caso de que el programa se cierre de manera inesperada, el archivo no se rompa.

### Trabajando con archivos de texto en Python

`encoding = "utf-8"` Sirve para que Python pueda soportar caracteres del idioma español, como la "ñ" y letras con tilde.

### Quiz 5

- ¿Qué letra simboliza el modo de escritura sin sobrescritura de un archivo en Python?: A
- ¿Qué método se utiliza para escribir una línea en un archivo de texto en Python?: write()
- El parámetro `encoding` de la función `open` es: opcional

## Conclusiones

### Reto Final: Juego del Ahorcado o Hangman Game

`os.system('cls')` -> Windows
`os.system('clear')` -> Unix
