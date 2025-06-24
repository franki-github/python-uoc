# Tema 2. Trabajo con datos en Python

## 🗒️ Requisitos

Para realizar los ejercicios de este tema deberás haber realizado los ejercicios de los temas anteriores.

### Librerias

Para instalar las librerías necesarias para este tema debes ejecutar el siguiente comando en el terminal:

```bash
pip install -r requirements.txt
```

> Nota: El archivo 'requirements.txt' no está dentro de ninguna carpeta.

## 📝 Enunciados

Los ejercicios los encontrarás organizados por carpetas según los apartados del tema. Cada ejercicio se presentará en un fichero python, que incluirá un comentario con el enunciado del ejercicio. 

Los apartados del tema junto con los ejercicios son los siguientes:

| Apartado | Ejercicios                                                     |
| -------- |----------------------------------------------------------------|
| a. Librerías para trabajo de datos en Python               | [ej2a1](2a/ej2a1.py) [ej2a2](2a/ej2a2.py) [ej2a3](2a/ej2a3.py) [ej2a4](2a/ej2a4.py) [ej2a5](2a/ej2a5.py) [ej2a6](2a/ej2a6.py)|
| b. Captura de datos                                       | [ej2b1](2b/ej2b1.py) [ej2b2](2b/ej2b2.py) [ej2b3](2b/ej2b3.py) [ej2b4](2b/ej2b4.py) [ej2b5](2b/ej2b5.py) |
| c. Preprocesamiento de datos                              | [ej2c1](2c/ej2c1.py) [ej2c2](2c/ej2c2.py) [ej2c3](2c/ej2c3.py) [ej2c4](2c/ej2c4.py) [ej2c5](2c/ej2c5.py) [ej2c6](2c/ej2c6.py) |
| d. Análisis de datos                                      | [ej2d1](2d/ej2d1.py) [ej2d2](2d/ej2d2.py) [ej2d3](2d/ej2d3.py) [ej2d4](2d/ej2d4.py) [ej2d5](2d/ej2d5.py) [ej2d6](2d/ej2d6.py) [ej2d7](2d/ej2d7.py) |
| e. Visualización de datos                                 | [ej2e1](2e/ej2e1.py) [ej2e2](2e/ej2e2.py) [ej2e3](2e/ej2e3.py) |
| f. Persistencia de datos   |  [ej2f1](2f/ej2f1.py) [ej2f2](2f/ej2f2.py) [ej2f3](2f/ej2f3.py)|

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta. 

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor. 

Si tienes alguna duda sobre cómo ejecutar los tests o cómo enviar los cambios a GitHub, consulta el ejercicio del Tema 0. Si todavía tienes algun comentario o problema, puedes escribir tu consulta en la plataforma de Preguntas y Respuestas de la Escuela de Programación.

## 💻 Comandos
En la siguiente sección se presentan algunos comandos útiles para el desarrollo de la actividad. 

### Git

Con el fin de actualizar los repositorios locales con la última versión de código fuente, ejecute:

```bash
git pull
```

Para agregar los cambios realizados en los archivos, ejecute:

```bash
git add .
```

Para añadir un mensaje a los cambios realizados localmente, ejecute:

```bash
git commit -m "Mensaje"
```

Para sincronizar nuestras modificaciones con el repositorio remoto, ejecute:
```bash
git push
```

### Python

Para ejecutar las pruebas unitarias:
```bash
pytest 
```
En caso de tener algún problema, puedes probar ejecutar la función con la instrucción `python -m` delante, por ejemplo:

```bash
python -m pytest 
```
```bash
python -m pip install -r requirements.txt
```
Más información sobre cómo ejecutar las pruebas unitarias, consulte el ejercicio del tema 0.
