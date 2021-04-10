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

```python
# This file must be used with "source bin/activate" *from bash*
# you cannot run it directly
```

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
