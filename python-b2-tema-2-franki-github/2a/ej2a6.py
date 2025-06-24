"""
Enunciado:

Explora el análisis avanzado de datos y la aplicación de ajustes no lineales mediante el uso de SciPy. Este ejercicio se
centra en ajustar una función gaussiana a un conjunto de datos usando el módulo scipy.optimize.curve_fit y en calcular
la integral de esta curva con scipy.integrate.quad.

Implementar la función gaussian_fit_and_integration(data_x, data_y) que realice lo siguiente:
    Ajuste de Curva Gaussiana: Utilizar scipy.optimize.curve_fit para ajustar una curva gaussiana a los datos.
    Integración Numérica: Calcular la integral de la curva gaussiana ajustada sobre el rango de data_x utilizando
    scipy.integrate.quad.

Además, implementar la función plot_gaussian_fit(data_x, data_y, gaussian_params) para visualizar los datos originales
y la curva gaussiana ajustada.

Parámetros:
    data_x (List[float]): Lista de valores en el eje x.
    data_y (List[float]): Lista de valores en el eje y correspondientes a data_x.
    gaussian_params (Tuple[float]): Parámetros (amplitud, centro, ancho) de la curva gaussiana ajustada.

Ejemplo:
    Entrada:
        data_x = np.linspace(-5, 5, 100)
        data_y = 3 * np.exp(-(data_x - 1)**2 / (2 * 1.5**2)) + np.random.normal(0, 0.2, 100)
    Ejecución:
        gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
        plot_gaussian_fit(data_x, data_y, gaussian_params)
    Salida:
        Un gráfico mostrando los datos originales y la curva gaussiana ajustada.
        La integral de la curva gaussiana ajustada.
"""

from scipy import optimize, integrate
import numpy as np
import matplotlib.pyplot as plt
import typing as t


def gaussian(x: float, amplitude: float, mean: float, stddev: float) -> float:
    # Write here your code
    return amplitude * np.exp(-((x - mean) ** 2) / (2 * stddev ** 2))

    pass

def gaussian_fit_and_integration(
    data_x: t.List[float], data_y: t.List[float]
) -> t.Tuple[t.Tuple[float], float]:
    # Write here your code
    # Ajuste de la curva gaussiana
    initial_guess = [1, 0, 1]  # Amplitud, media, desviación estándar   
    params, _ = optimize.curve_fit(gaussian, data_x, data_y, p0=initial_guess)
    # Calcular la integral de la curva gaussiana ajustada
    integral, _ = integrate.quad(gaussian, min(data_x), max(data_x), args=tuple(params))
    return params, integral  # type: ignore
    pass


def plot_gaussian_fit(
    data_x: t.List[float], data_y: t.List[float], gaussian_params: t.Tuple[float]
):
    # Write here your code
    # Graficar los datos originales
    plt.scatter(data_x, data_y, label='Datos Originales', color='blue', s=10)
    # Graficar la curva gaussiana ajustada
    x_fit = np.linspace(min(data_x), max(data_x), 100)
    y_fit = gaussian(x_fit, *gaussian_params)
    plt.plot(x_fit, y_fit, label='Curva Gaussiana Ajustada', color='red')
    # Configurar el gráfico
    plt.title('Ajuste de Curva Gaussiana')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.legend()
    plt.show()

    pass


#Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
data_x = np.linspace(-5, 5, 100)
data_y = 3 * np.exp(-(data_x - 1) ** 2 / (2 * 1.5 ** 2)) + np.random.normal(0, 0.2, 100)
gaussian_params, integral = gaussian_fit_and_integration(data_x, data_y)
print("Integral de la curva gaussiana ajustada:", integral)
plot_gaussian_fit(data_x, data_y, gaussian_params)
