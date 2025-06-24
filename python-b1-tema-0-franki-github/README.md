## 🗒️ Requisitos

Para realizar este ejercicio, deberás haber repasado los conceptos indicados en los materiales teóricos del tema. En concreto, deberás haber visto los siguientes conceptos:

- Instalación de Python. 
- ¿Qué es un IDE? Instalación del IDE
- ¿Qué es un sistema de control de versiones? Instalación de Git
- ¿Qué es GitHub y cómo se usa?

### Librerias

Para instalar las librerías necesarias para este tema debes ejecutar el siguiente comando en el terminal:

`pip install -r requirements.txt`

> Nota: El archivo 'requirements.txt' no está dentro de ninguna carpeta.

## 📝 Enunciado

Los ejercicios los encontrarás organizados por carpetas según los apartados del tema. Cada ejercicio se presentará en un fichero python, que incluirá un comentario con el enunciado del ejercicio. 

En este primer tema solamente encontrarás un ejercicio:

| Apartado                 | Ejercicios           |
| ------------------------ | -------------------- |
| a. Entorno de desarrollo | [ej0a1](0a/ej0a1.py) |

Para ayudarte a su resolución, hemos preparado unos **tests** que comprobarán que tu solución es correcta. En la sección [Cómo ejecutar los tests](#cómo-ejecutar-los-tests) describimos cómo hacerlo.

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, puedes enviar tus cambios para que se registren en la plataforma y, si fuera necesario, ser revisados y corregidos por tu profesor. En la sección [Entregar ejercicio](#entregar-ejercicio) describimos cómo has de enviar tu solución al ejercicio.


## 🛠️ Cómo ejecutar los tests

Para cada ejercicio encontrarás un fichero de test que te ayudará a comprobar si tu solución es correcta. Los ficheros de tests se encuentran en la misma carpeta que los ficheros de ejercicios y su nombre es el mismo pero con sufijo `_test.py`. Así, el fichero `ej0a1_test.py` tiene los tests para el ejercicio `ej0a1`.

Para ejecutar los tests debes utilizar el comando `pytest` desde la raíz del proyecto. Tienes varias formas de lanzar los tests, dependiendo del número de ejercicios que quieres comprobar.

### Ejecutar los tests de un ejercicio

Si quieres ejecutar los tests de un ejercicio deberás ejecutar el comando `pytest` indicando la carpeta y el fichero de test. No te preocupes si parece mucha información, todos los nombres siguen el mismo patrón para ayudarte a lanzar el test.

Por ejemplo, para lanzar el test del ejercicio `ej0a1`, deberás ejecutar el siguiente comando:

```bash
pytest 0a/ej0a1_test.py
```

Fíjate que como argumento a `pytest` le pasamos la carpeta `0a` y el fichero `ej0a1_test.py`. El comando `pytest` ejecutará los tests que encuentre en el fichero `ej0a1_test.py`. 

### Ejecutar todos los tests de un apartado

Para ejecutar todos los tests de un apartado deberás ejecutar el comando `pytest` indicando la carpeta del apartado. Por ejemplo, para lanzar los tests del apartado `0a`, deberás ejecutar el siguiente comando:

```bash
pytest 0a
```
Fíjate que como argumento a `pytest` le pasamos la carpeta `0a`. El comando `pytest` ejecutará los tests que encuentre en todos los ficheros `*_test.py` que encuentre en la carpeta `0a`. 

### Ejecutar todos los tests de todos los apartados

Para ejecutar todos los tests de todos los apartados deberás ejecutar el comando `pytest` desde la carpeta raíz del proyecto. Por ejemplo, para lanzar los tests de todos los apartados, deberás ejecutar el siguiente comando:

```bash
pytest 
```

### Resultados de la ejecución de los tests

El resultado de la ejecución del comando `pytest` te mostrará los tests ejecutados y su resultado.

Para el ejercicio ej0a1, una ejecución de tests **satisfactoria** mostraría algo como el siguiente texto. Fíjate que el texto muestra la plataforma, el directorio raíz y el número de tests ejecutados (en este caso 100%). La última línea indica que los tests han pasado.

```
================================= test session starts =================================
platform win32 -- Python 3.9.5, pytest-7.2.0, pluggy-1.0.0
rootdir: C:\git\UOC-Escola-de-Programacio\python-b1-tema0
collected 1 item

0a\ej0a1_test.py .                                                              [100%] 

================================== 1 passed in 0.02s ==================================
```

Por otro lado, una ejecución **incorrecta** sería como sigue. Imaginemos que la implementación de nuestro ejercicio solo devuelve `True` para valores superiores a 18 (sin incluir el propio valor 18). Esta sería una implementación incorrecta, así que una ejecución con tests fallidos mostraría algo como el siguiente texto. 

```
================================= test session starts =================================
platform win32 -- Python 3.9.5, pytest-7.2.0, pluggy-1.0.0
rootdir: C:\git\UOC-Escola-de-Programacio\python-b1-tema0
collected 1 item

0a\ej0a1_test.py F                                                              [100%]

====================================== FAILURES ======================================= 
_____________________________ TestCheckAge.test_check_age _____________________________ 

self = <ej_test.TestCheckAge testMethod=test_check_age>

    def test_check_age(self):
        self.assertEqual(check_age(15), False, "Should be False for age 15")
>       self.assertEqual(check_age(18), True, "Should be True for age 18")
E       AssertionError: False != True : Should be True for age 18

0a\ej0a1_test.py:7: AssertionError
=============================== short test summary info =============================== 
FAILED 0a/ej0a1_test.py::TestCheckAge::test_check_age - AssertionError: False != True : 
Should be True for age 18
================================== 1 failed in 0.12s ================================== 
```

Fíjate que la organización del texto que se muestra es muy parecida: la plataforma, el directorio raíz y el número de tests ejecutados (en este caso 100%). Sin embargo, ha habido un fallo, indicado en la sección `FAILURES`, en concreto en el test indicado con el carácter `>` (y con el mensaje `False != True : Should be True for age 18`). Eso te da pistas para comprobar cómo se comporta tu función con dicho valor. 

## 📦 Entregar ejercicio

Para entregar el ejercicio, sigue estos pasos. 

1. Guarda el fichero `0a/ej0a1.py` pulsando CTRL+s

2. Añade el fichero `0a/ej0a1.py` para ser registrado en el sistema de control de versiones mediante el comando `git add 0a/ej0a1.py`.

3. Haz commit de los cambios realizados en el repositorio local con el comando `git commit -m "Submitting exercise"`.

4. Envia los cambios al repositorio remoto con el comando `git push`.

Tu ejercicio ya está entregado, el profesor podrá revisarlo si es necesario. 

Desde la web de este repositorio en GitHub podrás ver que se ha generado un pull request llamado **Feedback**, el cual te permite ver también el resultado de la ejecución de los tests.
