from interpolation import bilinear_interpolation

MAX_LATITUDE = 2
MIN_LATITUDE = -20

MAX_LONGITUDE = -66
MIN_LONGITUDE = -83


def calculate_orthometric_height(model, latitude, longitude, h):
    
    if(latitude < MIN_LATITUDE or latitude > MAX_LATITUDE):
        raise ValueError("La latitud esta fuera de los limites del modelo ")
    
    if(longitude < MIN_LONGITUDE or longitude > MAX_LONGITUDE):
        raise ValueError("La longitud esta fuera de los limites del modelo ")
    
    i, j, i_trunc, j_trunc = model.calculate_indices(latitude, longitude)

    NA, NB, NC, ND = model.get_vertices(i, j)

    t, u = model.calculate_tu(latitude, longitude, NA, NB, ND)

    N = bilinear_interpolation(NA, NB, NC, ND, t, u)

    orthometric_height = h - N

    return {
        "Latitude": latitude,
        "Longitude": longitude,
        "Ellipsoidal Height": h,

        "Index_i": i,
        "Index_j": j,
        "Truncated_index_i": i_trunc,
        "Truncated_index_j": j_trunc,

        "NA": NA,
        "NB": NB,
        "NC": NC,
        "ND": ND,

        "t": t,
        "u": u,

        "Geoid_undulation": N,
        "Orthometric_height": orthometric_height


    }

    










    