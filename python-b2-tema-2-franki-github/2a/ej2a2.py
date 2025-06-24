"""
Enunciado:
Utiliza NumPy para crear y manipular matrices. Implementa dos funciones, create_matrices() y manipulate_matrices().
La función create_matrices() debe crear una matriz de ceros de tamaño 3x3, una matriz de unos de tamaño 2x4, y una
matriz identidad de tamaño 4x4.
La función manipulate_matrices() debe modificar estas matrices:
En la matriz de ceros, cambia el valor del elemento en la fila 2, columna 2 al valor de 5;
 En la matriz de unos, cambia
toda la tercera columna a 3; y en la matriz identidad, cambia la diagonal secundaria a 2.

Parámetros:

    - La función create_matrices() no recibe parámetros y devuelve las tres matrices creadas.
    - manipulate_matrices(zeros_matrix: np.ndarray, ones_matrix: np.ndarray, identity_matrix: np.ndarray) recibe las
    tres matrices creadas y devuelve las tres matrices modificadas.

Nota: recomendamos anotar las dos funciones (como aprendimos en el B1). Los tipos correspondientes seran: 
para matrices de NumPy usaremos el objeto `np.ndarray` y para agrupar la salida de una función usaremos el objeto 
`typing.Tuple` para señalar que la salida de una función son más de una matriz. 

Ejemplo:
    def create_matrices() -> np.ndarray:
        ...

    def manipulate_matrices(
        zeros_matrix: np.ndarray, 
        ones_matrix: np.ndarray, 
        identity_matrix: np.ndarray
    ) -> t.Tuple[np.ndarray, np.ndarray, np.ndarray]:
        ...

    Entrada:
    zeros_matrix, ones_matrix, identity_matrix = create_matrices()
    manipulate_matrices(zeros_matrix, ones_matrix, identity_matrix)

    Salida:
    [array([[0. 0. 0.]
            [0. 5. 0.]
            [0. 0. 0.]]),
     array([[1. 1. 3. 1.]
            [1. 1. 3. 1.]]),
     array([[1. 0. 0. 2.]
            [0. 1. 2. 0.]
            [0. 2. 1. 0.]
            [2. 0. 0. 1.]])]
"""
import numpy as np
import typing as t


def create_matrices() -> t.Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Write here your code

    #matriz rellena de ceros, matriz rellena de unos y matriz identidad    
    zeros_matrix = np.zeros((3, 3))
    ones_matrix = np.ones((2, 4))
    identity_matrix = np.eye(4)

    return zeros_matrix, ones_matrix, identity_matrix  # type: ignore

    pass


def manipulate_matrices(
    zeros_matrix: np.ndarray, ones_matrix: np.ndarray, identity_matrix: np.ndarray
) -> t.Tuple[np.ndarray, np.ndarray, np.ndarray]:
    # Write here your code
    # Modificar la matriz de ceros, elemento en fila 2, columna 2 al valor de 5
    
    zeros_matrix[1, 1] = 5
    # Modificar la matriz de unos
    ones_matrix[:, 2] = 3
    # Modificar la matriz identidad
    identity_matrix[0, 3] = 2
    identity_matrix[1, 2] = 2   
    identity_matrix[2, 1] = 2
    identity_matrix[3, 0] = 2
    return zeros_matrix, ones_matrix, identity_matrix  # type: ignore
    pass


# Para probar el código:
zeros_matrix, ones_matrix, identity_matrix = create_matrices()
print("Matriz de ceros creada:\n", zeros_matrix)
print("Matriz de unos creada:\n", ones_matrix)
print("Matriz identidad creada:\n", identity_matrix)
print("*" * 50)
zeros_matrix_modif, ones_matrix_modif, identity_matrix_modif = manipulate_matrices(
    zeros_matrix,
    ones_matrix,
    identity_matrix
)
print("Matriz de ceros modificada:\n", zeros_matrix_modif)
print("Matriz de unos modificada:\n", ones_matrix_modif)
print("Matriz identidad modificada:\n", identity_matrix_modif)
