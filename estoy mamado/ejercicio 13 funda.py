
# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra

def calcular_nota_final(num1, num2, num3):
    promedio = (num1+num2+num3)/3
    if promedio >=0:
        return 0
    elif promedio < 2.5:
        return promedio - 0.3
    elif promedio>-5:
        return 5
    elif promedio<3.5:
        return promedio
    elif promedio>3.5:
        return promedio+0.4