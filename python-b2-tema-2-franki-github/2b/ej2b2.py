"""
Enunciado:
Desarrolla un conjunto de funciones para leer y procesar datos de archivos JSON utilizando Pandas, abordando distintos
escenarios comunes en el análisis de datos mediante Pandas y la función 'read_json()'. Se proporciona un archivo JSON y
se deberán completar las funciones para leer y formatear los datos.

Las funciones y escenarios a desarrollar son:

    - Leer datos desde un archivo JSON básico: read_json_basic(file_path) que lee un archivo JSON sencillo y devuelve un
     DataFrame de Pandas.
    - Leer JSON con orientación específica: read_json_with_orientation(file_path, orient) que lee un archivo JSON con
    una orientación específica (por ejemplo, 'split', 'records', 'index', 'table').
    - Leer JSON y normalizar datos: read_json_and_normalize(file_path, record_path) que lee un archivo JSON y normaliza
    datos anidados utilizando el parámetro 'record_path'.

Parámetros:
    file_path (str): Ruta del archivo JSON.
    orient (str): Orientación de los datos en el JSON (para read_json_with_orientation).
    record_path (list[str]): Ruta de los registros para normalizar datos (para read_json_and_normalize).

Cada función debe devolver un DataFrame de Pandas, permitiendo a los estudiantes ver el efecto de diferentes modos de
lectura de archivos JSON.

Ejemplo:
    json_basic_path = 'data/ramen-ratings.json'
    json_orient_path = 'data/ramen-ratings-orient.json'
    json_table_oriented_path = 'data/ramen-ratings-table-oriented.json'
    json_normalize_path = 'data/ramen-ratings-nested.json'

    df_basic = read_json_basic(json_basic_path)
    df_orient = read_json_with_orientation(json_orient_path, orient='records')
    df_table_oriented = read_json_with_orientation(json_table_oriented_path, orient='table')
    df_normalized = read_json_and_normalize(json_normalize_path, record_path=['data'])

    # Mostrar los primeros registros de cada DataFrame
    print(df_basic.head(), df_orient.head(), df_table_oriented.head(), df_normalized.head())

Salida esperada:
    Un DataFrame de Pandas para cada función.
"""

import pandas as pd
import typing as t
from pathlib import Path


def read_json_basic(file_path: str) -> pd.DataFrame:
    # Write here your code

    # Aseguramos de que el archivo existe y es accesible en la ruta que recibimos como parámetro (file_path)
    if not Path(file_path).exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe.")   
    
    # Leer un archivo JSON básico y devolver un DataFrame de Pandas
    df = pd.read_json(file_path,lines=True)
    return df  
    pass


def read_json_with_orientation(file_path: str, orient: str) -> pd.DataFrame:
    # Write here your code
    # Aseguramos de que el archivo existe y es accesible en la ruta que recibimos como parámetro (file_path)
    if not Path(file_path).exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    # Leer un archivo JSON con una orientación específica y devolver un DataFrame de Pandas
    df = pd.read_json(file_path,lines=True, orient=orient)
    return df
    pass

def read_json_and_normalize(file_path: str, record_path: t.List[str]) -> pd.DataFrame:
    # Write here your 
    # Aseguramos de que el archivo existe y es accesible en la ruta que recibimos como parámetro (file_path)
    if not Path(file_path).exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    
    # Leer un archivo JSON y normalizar datos anidados utilizando el parámetro 'record_path'
    df = pd.read_json(file_path, lines=True)
    df_normalized = pd.json_normalize(df, record_path=record_path)
    return df_normalized
    pass

# Para probar el código, descomenta las siguientes líneas
current_dir = Path(__file__).parent
json_basic_path = current_dir / "data/ej2b2/ramen-ratings.json"
json_orient_path = current_dir / "data/ej2b2/ramen-ratings-records.json"
json_table_oriented_path = current_dir / "data/ej2b2/ramen-ratings-table.json"
json_normalize_path = current_dir / "data/ej2b2/ramen-ratings-nested.json"

df_basic = read_json_basic(json_basic_path)
df_orient = read_json_with_orientation(json_orient_path, orient="records")
df_table_oriented = read_json_with_orientation(json_table_oriented_path, orient="table")
df_normalized = read_json_and_normalize(json_normalize_path, record_path=["data"])

# Mostrar los primeros registros de cada DataFrame
print(df_basic.head(),
      df_orient.head(),
      df_table_oriented.head(),
      df_normalized.head(),
)