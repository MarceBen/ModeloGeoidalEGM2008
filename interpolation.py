def bilinear_interpolation(NA, NB, NC, ND, t, u):

    return (((1-t)*(1-u))*NA) + ((t*(1-u))*NB) + (t*u*NC) + (((1-t)*u)*ND)