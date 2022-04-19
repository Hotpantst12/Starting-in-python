

def calcular_valor (tiempo):
    minuto_adicional = tiempo - 60
    if tiempo >= 1 and tiempo <= 15:
        return 500
    elif tiempo >= 16 and tiempo <= 30:
        return 1000
    elif tiempo >= 31 and tiempo <= 60:
        return 1400
    elif tiempo > 60:
        return 1200 + (minuto_adicional* 20)
print (calcular_valor(70))
