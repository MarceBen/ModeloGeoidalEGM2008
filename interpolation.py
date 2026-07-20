def bilinear_interpolation(NA, NB, NC, ND, t, u):

    NA = NA["N_ondulacion_m"]
    NB = NB["N_ondulacion_m"]
    NC = NC["N_ondulacion_m"]
    ND = ND["N_ondulacion_m"]

    return (((1-t)*(1-u))*NA) + ((t*(1-u))*NB) + (t*u*NC) + (((1-t)*u)*ND)