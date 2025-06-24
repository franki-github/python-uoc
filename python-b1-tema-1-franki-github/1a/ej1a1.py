'''
Enunciado:
Implementa la función 'fibonacci(fibonacci_number)' que contenga el algoritmo
de Fibonacci y reciba como parámetro un valor numérico entero llamado 
'fibonacci_number'  y devuelva el valor de la serie Fibonacci en esa posición.

Parámetros:
- fibonacci_number: Número entero positivo mayor a 0 que representa la
posición en la serie Fibonacci.

Ejemplo:
    Entrada:
    fibonacci(10)

    Salida:
    55

Enunciat:
Implementa la funció 'fibonacci(fibonacci_number)' que contingui l'algorisme
de Fibonacci i rebi com a paràmetre un valor numèric enter anomenat
'fibonacci_number' i torneu el valor de la sèrie Fibonacci en aquesta posició.

Paràmetres:
- fibonacci_number: Nombre enter positiu superior a 0 que representa la
posició a la sèrie Fibonacci.

Exemple:
     Entrada:
     fibonacci(10)

     Sortida:
     55

'''

def fibonacci(fibonacci_number):

    if (fibonacci_number == 0):
        return 0
    
    #f1=1,f2=1,f3=2,f4=3,f5=5,f6= 8
    #f7=13,f8=21,f9=34,f10=55

    num = fibonacci_number
        
    contador = 1

#dado un numero encontrar la suma de la serie de fibonacci
    serie = []

    while (contador <= fibonacci_number):
        
        if (contador > 2):
            a = contador - 2
            b = contador - 3
            numa = serie[a]
            numb = serie[b]
            numero = numa + numb            
            serie.append(numero)            
        else:
            serie.append(1)

        contador += 1
        var = len(serie)

    return serie[-1]
    pass

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script 
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
#print(fibonacci(0))
#print(fibonacci(1))
#print(fibonacci(6))
#print(fibonacci(10))