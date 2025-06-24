"""
Enunciado:
Desarrolla un conjunto de funciones para leer y procesar datos de bases de datos SQLite utilizando Pandas, abordando
distintos escenarios comunes en el análisis de datos. Se proporciona una base de datos SQLite y se deberán completar las
funciones para leer, formatear y consultar los datos.

Las funciones y escenarios a desarrollar son:
    - Leer datos desde una tabla específica: read_sqlite_table(file_path, table_name) que lee todos los registros de una
     tabla específica en una base de datos SQLite y devuelve un DataFrame de Pandas.
    - Ejecutar una consulta SQL específica: execute_sqlite_query(file_path, query) que ejecuta una consulta SQL
    personalizada en una base de datos SQLite y devuelve un DataFrame con los resultados.

Parámetros:
    - file_path (str): Ruta al archivo de la base de datos SQLite.
    - table_name (str): Nombre de la tabla a leer (para read_sqlite_table).
    - query (str): Consulta SQL a ejecutar (para execute_sqlite_query).

Cada función debe devolver un DataFrame de Pandas, permitiendo a los estudiantes ver el efecto de diferentes modos de
lectura de datos desde una base de datos SQLite.

Ejemplo:

    sqlite_db_path = 'data/ramen-ratings.db'
    df_from_table = read_sqlite_table(sqlite_db_path, 'ramen_ratings')
    df_from_query = execute_sqlite_query(sqlite_db_path, 'SELECT * FROM ramen_ratings WHERE Stars > 4')

Salida esperada:
    Un DataFrame de Pandas para cada función.
"""

import pandas as pd
import sqlite3
from pathlib import Path


def read_sqlite_table(file_path: str, table_name: str) -> pd.DataFrame:
    # Write here your code
    # Aseguramos de que el archivo existe y es accesible en la ruta que recibimos como parámetro (file_path)
    if not Path(file_path).exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    # Conectamos a la base de datos SQLite
    conn = sqlite3.connect(file_path)
    # Leemos la tabla especificada y devolvemos un DataFrame de Pandas
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    # Cerramos la conexión
    conn.close()
    return df  # Devolver el DataFrame con los datos de la tabla especificada
    pass


def execute_sqlite_query(file_path: str, query: str) -> pd.DataFrame:
    # Write here your code

    # Aseguramos de que el archivo existe y es accesible en la ruta que recibimos como parámetro (file_path)
    if not Path(file_path).exists():
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    # Conectamos a la base de datos SQLite
    conn = sqlite3.connect(file_path)
    # Ejecutamos la consulta SQL y devolvemos un DataFrame de Pandas
    df = pd.read_sql_query(query, conn)
    # Cerramos la conexión
    conn.close()
    return df  # Devolver el DataFrame con los resultados de la consulta SQL

    pass


# Para probar el código, descomenta las siguientes líneas
db_path = "data/ej2b3/ramen-ratings.db"
current_dir = Path(__file__).parent
sqlite_db_path = current_dir / db_path


df_from_table = read_sqlite_table(sqlite_db_path, "ramen_ratings")
df_from_query = execute_sqlite_query(
    sqlite_db_path, "SELECT * FROM ramen_ratings WHERE Stars >= 4"
)

# Mostrar la cantidad de registros
print(f"Registros en la tabla: {len(df_from_table)}")
print(f"Registros en la consulta: {len(df_from_query)}")
