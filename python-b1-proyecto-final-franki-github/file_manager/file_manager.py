
def read(self):
    
   #LEE un archivo en formato CSV y permite exportar su resultado como un Data Frame.
   # recibira cualquier archivo CSV de la aplicacion
    
    import pandas as pd
    import os
    
    # Define the path to the CSV file
    file_path = os.path.join("data", "cashiers.csv")
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    return df


def write(self, dataFrame):
    #CONVIERTE un Data Frame en un archivo CSV. 
    # Esta es una función opcional, se deja al estudiante la implementación.
    
    import pandas as pd
    import os
    
    # Define the path to save the CSV file
    file_path = os.path.join("data", "output.csv")
    
    # Write the DataFrame to a CSV file
    dataFrame.to_csv(file_path, index=False)