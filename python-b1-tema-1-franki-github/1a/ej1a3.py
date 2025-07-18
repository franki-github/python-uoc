'''
Enunciado:
Implementa una función llamada "invert_text(text_chain)" que reciba como
parámetro una cadena de texto de tipo string llamada 'text_chain' y devuelva
el texto invertido.

Parámetros:
- text_chain: Este parámetro solo admite strings.

Ejemplo:
    Entrada:
    invert_text('Hello world!')

    Salida:
    !dlrow olleH

Enunciat:
Implementa una funció anomenada "invert_text(text_chain)" que rebi com
paràmetre una cadena de text de tipus string anomenada 'text_chain' i torni
el text invertit.

Paràmetres:
- text_chain: Aquest paràmetre només admet strings.

Exemple:
     Entrada:
     invert_text('Hello world!')

     Sortida:
     !dlrow olleH

'''

def invert_text(text_chain:str):
    # Write here your code
    #obtenemos la longitud de la cadena recibida
    
    texto_invertido = ""

    for letra in text_chain:
            
        #recorremos el texto recibido y añadimos la letra al principio de la cadena invertida
        #arrastrando las letras a la izquierda
        texto_invertido = letra + texto_invertido
        print(texto_invertido)
        
    return texto_invertido
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(invert_text("Hello world!"))
