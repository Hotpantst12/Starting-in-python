




def potencia (base, exponente):
    rta: int
    i: float
    e: float
    if (exponente<=0):
        e = -1 * exponente
    else:
        e = exponente
    rta = 1
    i= 1
    while (i<=e):
        rta = rta*base
        i= i+1
    if (exponente<=0):
        rta=1.0/rta
    return rta
def potencia_uno(base, exponente):
    if (exponente<=0):
        rta = 1
        i=1
        while (i<=-1*exponente):
            rta = rta*base
            i= i+1
    return rta
print (potencia(2,-3))
