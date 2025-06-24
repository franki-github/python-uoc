'''
Enunciado:
Crea una función 'sum_odd_numbers(list_numbers)' que reciba como 
parámetro una lista de números positivos enteros llamada 'list_numbers'
y devuelva la suma de los números impares encontrados en la lista.

Parámetros:
- list_numbers: Lista de números enteros positivos.

Ejemplo:
    Entrada:
    sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

    Salida:
    30

Enunciat:
Crea una funció 'sum_odd_numbers(list_numbers)' que rebi com
paràmetre una llista de nombres positius enters anomenada 'list_numbers'
i torneu la suma dels números imparells trobats a la llista.


Paràmetres:
- list_numbers: Llista de nombres enters positius.

Exemple:
     Entrada:
     sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100])

     Sortida:
     30

'''

def sum_odd_numbers(list_numbers):
    # Write here your code
    num = 0
    acumula = 0

    for num in list_numbers:
        if (num % 2 != 0):
            acumula = acumula + num 
    return acumula
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(sum_odd_numbers([1, 2, 3, 4, 5, 10, 21, 100]))
