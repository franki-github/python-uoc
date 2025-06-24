# Tema 6. Herramientas y entornos de desarrollo

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

| Apartado      | Ejercicios                                                     |
|---------------|----------------------------------------------------------------|
| b. Depuración | [ej6b1](6b/ej6b1.py) [ej6b2](6b/ej6b2.py) [ej6b3](6b/ej6b3.py) |
| c. Librerías  | [ej6c1](6c/ej6c1.py) [ej6c2](6c/ej6c2.py) [ej6c3](6c/ej6c3.py) |

Además, cada ejercicio irá acompañado de uno o varios tests para comprobar que tu solución es correcta.

Cuando hayas propuesto una implementación para la función, ejecuta los tests para ver si tu solución es correcta. Para ello asegurate de estar ubicado en la carpeta del ejercicio correspondiente 6b/6c antes de ejecutar el comando `pytest`. Si no pasa los tests, vuelve a intentarlo revisando los errores que te comentan los tests.

Una vez termines el ejercicio, deberás enviar tus cambios para que se registren en la plataforma y que puedan ser corregidos por tu profesor.

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
