"""
Enunciado:
En este ejercicio deberás implementar la función `check_age(age)`, la cual 
recibe como parámetro `age`, que es un valor numérico y devuelve `True` si 
el valor es igual o superior a 18.

Parámetros:
age (int): Valor numérico que indica la edad de una persona

Ejemplo:
    Entrada:
    check_age(15)
    check_age(17)
    check_age(18)

    Salida:
    False
    False
    True    
    
Enunciat:
En aquest exercici hauràs d'implementar la funció `check_age(age)`, la qual 
rep com a paràmetre `age`, que és un valor numèric i retorna `True` si 
el valor és igual o superior a 18.

Paràmetres:
age (int): Valor numèric que indica l'edat d'una persona

Exemple:
    Entrada:
    check_age(15)
    check_age(17)
    check_age(18)

    Sortida:
    False
    False
    True

"""

def check_age(age):
    #write your code
    if (age >= 18):
        return True
    else:
        return False
    pass
    
  
# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(check_age(15))
#print(check_age(17))
#print(check_age(18))
