# David Ricardo Carvajal Rincon

# Calcular mediante una función el valor de la cuota mensual y mediante otra función el número de cuotas a pagar,
#por la realización de un préstamo en un banco con las siguientes condiciones: 
# si el préstamo es menor de $500000 se paga un interés de 10% sobre el total del préstamo y las cuotas mensuales
# quedan de un 3% del monto total. Si el préstamo está entre $500000 y $1000000 (inclusive) se paga un interés del 7% 
# y las cuotas quedan de un 5% del monto total. Y si el préstamo es superior a $1000000 se paga un interés del 4% 
# y las cuotas quedan de un 7% del monto total.

from os import pread


valor_interes: float
def calcular_cuota_mensual (prestamo, valor_interes):
    if prestamo < 500000:
        prestamo / 10
        prestamo * valor_interes
    elif prestamo == (500000 )or(1000000):
        prestamo / 7
        prestamo * valor_interes
    elif prestamo > 1000000:
        prestamo / 4
        prestamo * valor_interes
    return prestamo
    
print (calcular_cuota_mensual(400000,440000))
