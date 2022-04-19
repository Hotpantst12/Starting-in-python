
# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra

def calcular_valor(num1):
    minuto_adicional=num1-60
    if num1>=1 and num1<=15:
         return 500
    elif num1>=16 and num1<=30:
         return 1000
    elif num1>=31 and num1<=60:
         return 1400
    elif num1>60:
         return 12001 (minuto_adicional*20)