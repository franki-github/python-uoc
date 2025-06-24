'''
Enunciado:
Crea una función llamada "count_vowels(text_chain)" que reciba como parámetro
una cadena de texto de tipo string llamada 'text_chain' y retorne el número
de vocales, ya sean mayúsculas o minúsculas, sin tilde que se encuentren en dicha 
cadena de texto.

Parámetros:
- text_chain: Este parámetro admite únicamente strings.

Ejemplo: 
    Entrada:
    count_vowels('Hello world, this is an example.')

    Salida:
    9

Enunciat:
Crea una funció anomenada "count_vowels(text_chain)" que rebi com a paràmetre
una cadena de text de tipus string anomenada 'text_chain' i retorni el número
de vocals, ja siguin majúscules o minúscules, sense accent, que es trobin en 
aquesta cadena de text.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     count_vowels('Hello world, this is an example.')

     Sortida:
     9

'''

def count_vowels(text_chain:str):
    # Write here your code
    vocales = ['a', 'e', 'i', 'o', 'u']
    numero_vocales = 0

    for letra in text_chain:
        if letra.lower() in vocales:
            numero_vocales += 1
    
    return numero_vocales
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(count_vowels("Hello world, this is an example."))
