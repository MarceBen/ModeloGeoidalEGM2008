import pandas as pd
import math as mt
from pathlib import Path

class EGModel2008: # CLASE QUE CARGA EL MODELO GEOIDAL
    def __init__(self):
        self.vertices = None
        self.lambda0 = -83  # Longitud
        self.phi0 = -20 # Latitud
        self.delta = 0.0416666667


    def load_model(self): # CARGA LA GRILLA DESDE EL XLSX Y CONSTRUYE INDICES POR FILA Y COLUMNA

        path = Path(__file__).parent / "data" / "cuadro_vertices_grilla_EGM2008_Peruaa.xlsx"
        df = pd.read_excel(path, sheet_name="Vertices_Grilla")
        self.vertices = df.set_index(["Fila", "Columna"])

        print(f"Modelo cargado: {len(self.vertices)} vértices.")

    
    def calculate_indices(self, latitude, longitude): # CALCULA EL INDICE I Y J DE UNA LATITUD Y LONGITUD

        i = abs((longitude - self.lambda0 ) / self.delta) 
        j = abs((latitude - self.phi0) / self.delta)

        i_trunc = mt.trunc(i)
        j_trunc = mt.trunc(j)

        return i, j, i_trunc, j_trunc
    
    def get_vertices(self, i, j):

        NA = self.vertices.loc[(j, i)]
        NB = self.vertices.loc[(j, i+1)]
        NC = self.vertices.loc[(j+1, i+1)]
        ND = self.vertices.loc[(j+1, i)]

        return NA, NB, NC, ND
    
    def calculate_tu(self, latitude, longitude, NA, NB, ND):

        lambda0 = NA["Longitud"]
        lambda1 = NB["Longitud"]

        t = (longitude - lambda0) / (lambda1 - lambda0)

        phi0 = NA["Latitud"]
        phi1 = ND["Latitud"]

        u = (latitude - phi0) / (phi1 - phi0)

        return t, u





    

        



        


