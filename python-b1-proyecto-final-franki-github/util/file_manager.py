import pandas as pd
import os


#gestionamos la lectura de los ficheros csv
#los ficheros deben estar en la carpeta "data"
class CSVFileManager:
  def __init__(self,path: str):
      
      base_path = os.path.dirname(os.path.abspath(__file__))
      self.path = os.path.join(base_path, '..', 'data', path)
      
  def read(self) -> str:
      return pd.read_csv(self.path)
  
  def write(self,dataFrame):
     pass