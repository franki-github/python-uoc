"""
Implementa una función 'read_and_write', no recibe ningún parámetro debido a
que, dentro de la misma se debe solicitar la entrada de 2 datos mediante
teclado.

En el momento de solicitar el ingreso de los datos se debe considerar el
siguiente texto.
'Insert your name: ' El valor introducido debe ser de tipo str.
'Insert your age: ' El valor introducido debe ser de tipo int.

Se debe crear un archivo de texto 'file.txt' donde La información entrada
por consola debe ser guardada en dicho archivo y se debe imprimir por consola
desde el archivo de texto.

Parámetro:
No recibe ningún parámetro.

Ejemplo:
    Entrada:
        'Insert your name: ' Julio 
        'Insert your age: ' 30
    Salida:
        Julio
        30

Enunciat:

Implementa una funció 'read_and_write', no rep cap paràmetre a causa de
que, dins de la mateixa cal sol·licitar l'entrada de 2 dades mitjançant
teclat.

En el moment de sol·licitar l'ingrés de les dades s'ha de considerar el
següent text.
'Insert your name: ' El valor introduït ha de ser de tipus str.
'Insert your age: ' El valor introduït ha de ser de tipus int.

S'ha de crear un fitxer de text 'file.txt' on La informació entrada
per consola s'ha de guardar en aquest fitxer i s'ha d'imprimir per consola
des del fitxer de text.

Paràmetre:
No rep cap paràmetre.

Exemple:
     Entrada:
         'Insert your name: ' Juliol
         'Insert your age: ' 30
     Sortida:
         Juliol
         30

"""
import sys
import os

def read_and_write():
    # Write here your code
    # Solicitar el nombre y la edad al usuario
    name = ""
    age = 0
    
    while True:        
            name = input("Insert your name: ")
            
            if name.isalpha():
                break
            else:
                print("Invalid input. Por faver entra un nombre valido.")

    while True:        
            age = input("Insert your age: ")
            
            if age.isnumeric():
                
                break
            else:
                print("Invalid input. Por faver entra una edad.")
    

    
    # Crear el archivo de texto y escribir los datos
    with open("file.txt", "w") as file:
        file.write(name + "\n")
        file.write(age + "\n")
        
    # Leer el archivo de texto y mostrar su contenido
    with open("file.txt", "r") as file:
        content = file.readlines()
        for line in content:
            print(line.strip())  # Imprimir cada línea sin saltos de línea adicionales      
    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
read_and_write()
