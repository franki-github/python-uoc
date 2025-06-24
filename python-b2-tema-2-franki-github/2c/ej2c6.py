"""
Enunciado:
Desarrolla un conjunto de funciones para realizar y visualizar un análisis de componentes principales (PCA) utilizando
`sklearn.decomposition.PCA` en el conjunto de datos de viviendas. Este conjunto de datos contiene varias características
de viviendas en áreas suburbanas de Boston, y el objetivo es reducir la dimensionalidad de los datos para identificar
las principales componentes que explican la mayor parte de la varianza en el conjunto de datos.

Las funciones a desarrollar son:
1. Preparar los datos: `prepare_data_for_pca(file_path: str)` que lee el archivo CSV y prepara los datos eliminando
cualquier característica no numérica. Se debe saltar las primeras 14 filas del archivo CSV, que contienen información
adicional sobre el conjunto de datos.
2. Realizar PCA: `perform_pca(data, n_components: int)` que realiza PCA en los datos preparados, reduciendo a
`n_components` número de dimensiones, en este caso a 4 dimensiones.
3. Visualizar los resultados: `plot_pca_results(pca)` que visualiza los resultados de PCA, incluyendo la varianza
explicada por cada componente principal.

Parámetros:
    file_path (str): Ruta al archivo CSV que contiene los datos del dataset de viviendas.
    n_components (int): Número de componentes principales a retener en el análisis PCA.

Ejemplo de uso:
    pca = perform_pca(data, 4)
    plot_pca_results(pca)

Salida esperada:
    Una visualización de la varianza explicada por los componentes principales y, opcionalmente, una transformación de
    los datos originales proyectada en las principales componentes.
"""

from pathlib import Path
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


def prepare_data_for_pca(file_path: str) -> pd.DataFrame:
    # Write here your code
    # Leemos el archivo CSV, saltando las primeras 14 filas
    df = pd.read_csv(file_path, skiprows=14)
    # Eliminamos las columnas no numéricas
    df = df.select_dtypes(include=['float64', 'int64'])
    # Eliminamos filas con valores NaN
    df.dropna(inplace=True)
    # Reseteamos el índice del DataFrame
    df.reset_index(drop=True, inplace=True)
    return df  # Retornamos el DataFrame preparado para PCA
    pass


def perform_pca(data: pd.DataFrame, n_components: int) -> PCA:
    # Write here your 
    # Estandarizamos los datos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    # Creamos el objeto PCA y ajustamos los datos
    pca = PCA(n_components=n_components)
    pca.fit(scaled_data)
    # Transformamos los datos
    transformed_data = pca.transform(scaled_data)
    # Añadimos los componentes principales al DataFrame original
    pca_df = pd.DataFrame(transformed_data, columns=[f'PC{i+1}' for i in range(n_components)])
    # Retornamos el objeto PCA y el DataFrame transformado
    data.reset_index(drop=True, inplace=True)
    data = pd.concat([data, pca_df], axis=1)
    return pca, data  # Retornamos el objeto PCA y el DataFrame transformado
    pass


def plot_pca_results(pca: PCA) -> tuple:
    # Write here your code
    # Visualizamos la varianza explicada por cada componente principal
    plt.figure(figsize=(10, 6))
    plt.bar(range(1, len(pca.explained_variance_ratio_) + 1), pca.explained_variance_ratio_, alpha=0.7)
    plt.xlabel('Componentes Principales')
    plt.ylabel('Varianza Explicada')
    plt.title('Varianza Explicada por Componentes Principales')
    plt.xticks(range(1, len(pca.explained_variance_ratio_) + 1))
    
    plt.grid()
    plt.show()
    # Retornamos la figura y los ejes para posibles personalizaciones
    return plt.gcf(), plt.gca()  # Retornamos la figura y los ejes de la gráfica

    pass


# Para probar el código, descomenta las siguientes líneas
if __name__ == "__main__":
    current_dir = Path(__file__).parent
    FILE_PATH = current_dir / "data/housing.csv"
    dataset = prepare_data_for_pca(FILE_PATH)
    pca, dataset_pca = perform_pca(dataset, 4)
    _, _ = plot_pca_results(pca)
