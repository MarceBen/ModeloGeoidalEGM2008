from egm2008 import EGModel2008
from interpolation import bilinear_interpolation

# Carga de las grillas del modelo xlsx
try:
    
    model = EGModel2008()
    model.load_model()

except FileNotFoundError as msg:

    print(msg)
    exit()


# Ingreso de datos por el usuario
try:
    latitude = float(input("Ingrese la latitud: "))
except ValueError:
    print("La latitud debe ser un valor numérico.")
    exit()

try:
    longitude = float(input("Ingrese la longitud: "))
except ValueError:
    print("La longitud debe ser un valor numérico.")
    exit()

try:
    h = float(input("Ingrese la altura elipsoidal: "))
except ValueError:
    print("La altura elipsoidal debe ser un valor numérico.")
    exit()

if(latitude < -20 or latitude > 2):
    print("El valor ingresado no comprende los limites del modelo. ")
    exit()

if(longitude < -83 or longitude > -66):
    print("El valor ingresado no comprende los limites del modelo. ")
    exit()


# Calculo de los indices donde se encuentra el punto (en decimales y truncdos)
i, j, i_trunc, j_trunc = model.calculate_indices(latitude, longitude)
print(f"El punto se encuentra entre las columnas: {i_trunc} y {i_trunc + 1}")
print(f"El punto se encuentra entre las filas: {j_trunc} y {j_trunc + 1}")

# Calculo de los vertices de la grilla donde se encuentra el punto
try:
    NA, NB, NC, ND = model.get_vertices(i_trunc, j_trunc)
except ValueError as msg:
    print(msg)
    exit()

NA_ondulation = NA["N_ondulacion_m"]
NB_ondulation = NB["N_ondulacion_m"]
NC_ondulation = NC["N_ondulacion_m"]
ND_ondulation = ND["N_ondulacion_m"]


# Calculo de t y u para la interpolacion
t, u = model.calculate_tu(latitude, longitude, NA, NB, ND)

# Calculo de la interpolacion lineal
N = bilinear_interpolation(NA_ondulation, NB_ondulation, NC_ondulation, ND_ondulation, t, u)

# Calculo de la altura ortometrica
H_ortometrica = h - N

# Resultados
print("\n========== RESULTADOS ==========\n")

print("Datos ingresados")
print(f"Latitud: {latitude}")
print(f"Longitud: {longitude}")
print(f"Altura elipsoidal: {h} m")

print("\nÍndices calculados")
print(f"i: {i}")
print(f"j: {j}")
print(f"i truncado: {i_trunc}")
print(f"j truncado: {j_trunc}")

print("\nUbicación en la grilla")
print(f"El punto se encuentra entre las columnas {i_trunc} y {i_trunc + 1}")
print(f"El punto se encuentra entre las filas {j_trunc} y {j_trunc + 1}")

print("\nVértice A")
print(NA)

print("\nVértice B")
print(NB)

print("\nVértice C")
print(NC)

print("\nVértice D")
print(ND)

print("\nOndulaciones de los vértices")
print(f"NA: {NA_ondulation} m")
print(f"NB: {NB_ondulation} m")
print(f"NC: {NC_ondulation} m")
print(f"ND: {ND_ondulation} m")

print("\nParámetros de interpolación")
print(f"t: {t}")
print(f"u: {u}")

print("\nResultados finales")
print(f"Ondulación geoidal (N): {N} m")
print(f"Altura ortométrica (H): {H_ortometrica} m")





