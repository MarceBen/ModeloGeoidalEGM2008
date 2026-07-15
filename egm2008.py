import pandas as pd
import math as mt
from pathlib import Path

class EGModel2008: # CLASE QUE CARGA EL MODELO GEOIDAL
    def __init__(self):
        self.vertices = None
        self.lambda0 = -83  # Longitud
        self.phi0 = -20 # Latitud
        self.delta = 0.0416666667


    def load_model(self): # CARGA LA GRILLA DESDE EL XLXX Y CONSTRUYE INDICES POR FILA Y COLUMNA
        path = Path(__file__).parent / "data" / "cuadro_vertices_grilla_EGM2008_Peruaa.xlsx"
        df = pd.read_excel(path, sheet_name="Vertices_Grilla")
        self.vertices = df.set_index(["Fila", "Columna"])

        print(f"Modelo cargado: {len(self.vertices)} vértices.")

    
    def calculate_indices(self, latitude, longitude): # CALCULA EL INDICE I Y J DE UNA LATITUD Y LONGITUD

        i = abs((longitude - self.lambda0 ) / self.delta) 
        j = abs((latitude - self.phi0) / self.delta)

        i_trunc = mt.trunc(i)
        j_trunc = mt.trunc(j)

        return i_trunc, j_trunc


    

        



        


