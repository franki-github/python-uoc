"""
Enunciado:
Desarrolla un conjunto de funciones matemáticas para calcular el máximo común divisor (MCD) y el mínimo común múltiplo
(MCM) de un conjunto de números enteros, mediante la estrategia algoritmica Bottom up.

Funciones a desarrollar:
- `mcd(a: int, b: int) -> int`:
    Descripción:
    Calcula el máximo común divisor de dos números enteros utilizando el algoritmo de Euclides.
    Parámetros:
        - `a` (int): Primer número entero.
        - `b` (int): Segundo número entero.

- `mcd_list(numbers: List[int]) -> int`:
    Descripción:
    Extiende el cálculo del máximo común divisor a una lista de números enteros, aplicando secuencialmente el MCD a
    pares de números de la lista.
    Parámetros:
        - `numbers` (List[int]): Lista de números enteros.

- `mcm(a: int, b: int) -> int`:
    Descripción:
    Determina el mínimo común múltiplo de dos números enteros.
    Parámetros:
        - `a` (int): Primer número entero.
        - `b` (int): Segundo número entero.

- `mcm_list(numbers: List[int]) -> int`:
    Descripción:
    Calcula el mínimo común múltiplo de una lista de números enteros.
    Parámetros:
        - `numbers` (List[int]): Lista de números enteros.

Ejemplo:
    numbers = [4, 6, 8, 20]
    print(f"The GCD of {numbers} is {gcd_list(numbers)}.")
    print(f"The LCM of {numbers} is {lcm_list(numbers)}.")


Salida esperada:
- Cálculo del máximo común divisor y del mínimo común múltiplo de un conjunto de números enteros.
"""

from typing import List


def mcd(a: int, b: int) -> int:
    while b:
        resto = b % a
        #Ahora el valor a será el antiguo b y b será el módulo anteriormente calculado
        a, b = b, resto
    # Cuando b es 0, a contiene el MCD
        if resto == 0:
            return a
        
        
    return a


def mcd_list(numbers: List[int]) -> int:
    result = numbers[0]
    for number in numbers[1:]:
        result = mcd(result, number)
        if result == 1:  # Si el MCD es 1, no hay necesidad de seguir
            return 1
    return result


def mcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // mcd(a, b)
    result = mcd(a, b)

    return 


def mcm_list(numbers: List[int]) -> int:
    result = numbers[0]
    if result == 0:  # Si el primer número es 0, el MCM es 0
        return 0
    for number in numbers[1:]:
        result =  mcm(result, number)
        if result == 0:  # Si el MCM es 0, no hay necesidad de seguir
            return 0
    return result


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    numbers = [4, 6]
    print(f"The MCD of {numbers} is ")

    print(f"The MCD of {numbers} is {mcd_list(numbers)}.")
    print(f"The MCM of {numbers} is {mcm_list(numbers)}.")
