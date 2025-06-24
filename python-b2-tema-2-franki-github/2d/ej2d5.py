"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de regresión lineal utilizando 
`sklearn.linear_model.LinearRegression` en el conjunto de datos de viviendas. Este conjunto de datos contiene varias
características de viviendas en áreas suburbanas de Boston, y el objetivo es predecir el valor medio de las viviendas
(`MEDV`) a partir de estas características.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_regression(data: pd.DataFrame)` que lee el archivo CSV, divide los datos en
características (X) y el objetivo (y) siendo `MEDV`. Además, realiza un split de entrenamiento y prueba con una
proporción de 80/20.
2. Realizar la regresión lineal: `perform_linear_regression(X_train, y_train)` que entrena un modelo de regresión
lineal con los datos de entrenamiento.
3. Evaluar el modelo: `evaluate_regression_model(model, X_test, y_test)` que evalúa el rendimiento del modelo con los
datos de prueba, devolviendo métricas como el R^2 y RMSE.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de viviendas.

Ejemplo de uso:
    X_train, X_test, y_train, y_test = prepare_data_for_regression('./data/housing.csv')
    model = perform_linear_regression(X_train, y_train)
    r_squared, rmse = evaluate_regression_model(model, X_test, y_test)
    print(f'R^2 del modelo: {r_squared}, RMSE: {rmse}')

Salida esperada:
    Los valores de R^2 y RMSE indicando el rendimiento del modelo en el conjunto de prueba.
"""

from pathlib import Path
from typing import Tuple
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error


def prepare_data_for_regression(data: pd.DataFrame) -> Tuple:
    # Write here your code
    pass


def perform_linear_regression(X_train, y_train) -> LinearRegression:
    # Write here your code
    pass


def evaluate_regression_model(model, X_test, y_test) -> Tuple[float, float]:
    # Write here your code
    pass


# Para probar el código, descomenta las siguientes líneas
# if __name__ == '__main__':
#     current_dir = Path(__file__).parent
#     file_path = current_dir / 'data/housing.csv'
#     data = pd.read_csv(file_path, skiprows=14)
#     X_train, X_test, y_train, y_test = prepare_data_for_regression(data)
#     model = perform_linear_regression(X_train, y_train)
#     r_squared, rmse = evaluate_regression_model(model, X_test, y_test)
#     print(f'R^2 del modelo: {r_squared}, RMSE: {rmse}')
