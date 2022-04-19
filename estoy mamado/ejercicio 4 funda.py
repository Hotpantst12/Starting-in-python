
# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra

def sueldo_horas_trabajadas(x):
    horas_extra=x-40
    hora=6500
    recargo=8450
    if x<=40:
        return x*hora
    elif x>40:
        return 260000+(recargo *horas_extra)