"""
Enunciado:
Explora el análisis de datos mediante la realización de una regresión lineal y la interpolación de un conjunto de datos.
Este ejercicio se centra en el uso de scipy.optimize para llevar a cabo una regresión lineal y en la aplicación de
scipy.interpolate para la interpolación de datos.

Implementa la función linear_regression_and_interpolation(data_x, data_y) que realice lo siguiente:
    - Regresión Lineal: Ajustar una regresión lineal a los datos proporcionados.
    - Interpolación: Crear una interpolación lineal de los mismos datos.

Adicionalmente, implementa la función plot_results(data_x, data_y, results) para graficar los datos originales,
la regresión lineal y la interpolación.

Parámetros:
    - data_x (List[float]): Lista de valores en el eje x.
    - data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    - results (Dict): Resultados de la regresión lineal e interpolación.

Ejemplo:
    - Entrada:
        data_x = np.linspace(0, 10, 100)
        data_y = 3 - data_x + 2 + np.random.normal(0, 0.5, 100) # Datos con tendencia lineal y algo de ruido
    - Ejecución:
        results = linear_regression_and_interpolation(data_x, data_y)
        plot_results(data_x, data_y, results)
    - Salida:
        Un gráfico mostrando los datos originales, la regresión lineal y la interpolación.
"""

from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plt
import typing as t


def linear_regression_and_interpolation(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Dict[str, t.Any]:
    # Write here your code
    # Ajuste de regresión lineal
    coefficients = np.polyfit(data_x, data_y, 1)
    linear_fit = np.poly1d(coefficients)
    # Interpolación lineal
    linear_interp = interpolate.interp1d(data_x, data_y, kind='linear', fill_value='extrapolate')
    # Crear un diccionario con los resultados
    results = {
        'linear_fit': linear_fit,
        'linear_interp': linear_interp,
        'coefficients': coefficients
    }
    return results  # type: ignore

    pass


def plot_results(data_x: t.List[float], data_y: t.List[float], results: t.Dict):
    # Write here your 
    # Graficar los datos originales
    plt.scatter(data_x, data_y, label='Datos Originales', color='blue', s=10)
    # Graficar la regresión lineal
    x_fit = np.linspace(min(data_x), max(data_x), 100)
    y_fit = results['linear_fit'](x_fit)
    plt.plot(x_fit, y_fit, label='Regresión Lineal', color='red')
    # Graficar la interpolación
    y_interp = results['linear_interp'](x_fit)
    plt.plot(x_fit, y_interp, label='Interpolación Lineal', color='green', linestyle='--')
    # Configurar el gráfico
    plt.title('Regresión Lineal e Interpolación de Datos')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.grid()
    plt.show()


    pass


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
data_x = np.linspace(0, 10, 100)
data_y = 3 * data_x + 2 + np.random.normal(0, 2, 100)
results = linear_regression_and_interpolation(data_x, data_y)
plot_results(data_x, data_y, results)
