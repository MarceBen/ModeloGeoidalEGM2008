import pandas as pd
from pathlib import Path

class EGModel2008:
    def __init__(self):
        self.vertices = None
        self.lambda0 = -83
        self.phi0 = -20
        self.delta = 0.0416666667

    def load_model(self):
        path = Path(__file__).parent / "data" / "cuadro_vertices_grilla_EGM2008_Peruaa.xlsx"
        df = pd.read_excel(path, sheet_name="Vertices_Grilla")
        self.vertices = df

        print(f"Modelo cargado: {len(self.vertices)} vértices.")



        


