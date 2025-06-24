"""
Enunciado:
Implementa dos funciones: 'count_letters(names)' y 'create_log(names)'.
En primer lugar, utilizando la librería logging, implementa una función 
'count_letters(names)' que recibe como parámetro 'names' que es una lista de 
strings con nombres. La función debe contar cuántas veces aparece cada letra 
en todos los nombres de la lista. La función debe devolver un diccionario con 
la frecuencia de cada letra.

En segundo lugar, la función 'create_log(names)' recibe también una lista
de strings con nombres, llama a la función 'count_letters(names)' y almacena
el diccionario generado en el archivo 'production.log' en formato de 
registro de nivel DEBUG.

Una vez se tenga el diccionario de la función 'count_letters(names)', debes
guardarlo con el siguiente código:
logging.info(f'Letter counts: {letter_counts}')

Parámetro:
    names: lista de strings.

Ejemplo:
    Entrada:
        ["Juan", "Pedro", "Marta"]
    Salida:
        Existe un fichero "production.log" que contiene:
        DEBUG:root:Letter counts: {'J': 1, 'u': 1, 'a': 3, 'n': 1, 'P': 1, 'e': 1, 'd': 1, 'r': 2, 'o': 1, 'M': 1, 't': 1}

Nota: Verificar que el archivo de logs se haya creado.


Enunciat:
Implementa dues funcions: 'count_letters(names)' i 'create_log(names)'.
En primer lloc, utilitzant la llibreria logging, implementa una funció 
'count_letters(names)' que rep com a paràmetre 'names' que és una llista de 
strings amb noms. La funció ha de comptar quantes vegades apareix cada lletra 
en tots els noms de la llista. La funció ha de retornar un diccionari amb 
la freqüència de cada lletra.

En segon lloc, la funció 'create_log(names)' rep també una llista
de strings amb noms, crida a la funció 'count_letters(names)' i emmagatzema
el diccionari generat en l'arxiu 'production.log' en format de 
registre de nivell DEBUG.

Un cop es tingui el diccionari de la funció 'count_letters(names)', has de
guardar-ho amb el codi següent:
logging.info(f'Letter counts: {letter_counts}')

Paràmetre:
     names: llista de strings.

Exemple:
     Entrada:
         ["Juan", "Pedro", "Marta"]
     Sortida:
        Existeix un fitxer "production.log" que conté:
        DEBUG:root:Letter counts: {'J': 1, 'u': 1, 'a': 3, 'n': 1, 'P': 1, 'e': 1, 'd': 1, 'r': 2, 'o': 1, 'M': 1, 't': 1}

Nota: Verifiqueu que el fitxer de logs s'hagi creat.
"""
import logging

def count_letters(names):
    letter_counter ={}
    # Para cada palabra de la lista...
    for name in names:
        # Para cada letra de la palabra...
        for letter in name:
            # Si no existe en el dict. la agrego , si existe le sumo.
            if letter in letter_counter:
                letter_counter[letter] = letter_counter[letter] + 1
            else:
                letter_counter[letter] = 1
    # retorno el diccionario
    return letter_counter


def create_log(names):
    # Configuro el logging: fichero de slida y el nivel de log.
    logging.basicConfig(level=logging.DEBUG, filename="production.log",)
    letter_counter = count_letters(names)
    # Escribo a log.
    logging.debug(f"Letter counts: {letter_counter}")


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# create_log(["Juan", "Pedro", "Marta"])
