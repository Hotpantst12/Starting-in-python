# Suponga que las tarifas de una compañía de gas se basan en el consumo de acuerdo con la siguiente información:

# los primeros 70 metros cúbicos de gas usado tiene un costo de 2000 pesos y esto se constituye

# en tarifa básica (si consume menos de 70 metros cúbicos igual se cobrará los 2000 pesos)

# para los consumos entre 70 y 200 metros cúbicos se cobra a 50 pesos el metro cúbico,

# y para consumos por encima de 200 metros cúbicos de gas consumidos

# se cobrará a 80 pesos por metro cúbico. Dada la lectura del contador al inicio de mes y al final del mes 

# (dos números enteros el primero menor que el segundo), en metros cúbicos, calcule el valor de la factura.

# David Ricardo Carvajal Rincon

# Belen nathalia pedraza becerra

#Metroscubicos = int(input('ingrese los metros cubicos de gas que se han consumido en este mes: '))

def calcular_valor_consumo(num1, num2):
    if num1 and num2 <=70:
        return 2000
    elif num1 and num2>200:
        return num1 * 80 and num2*80
    elif num1 and num2>70<=200:
        return num1*50 and num2*50

print (calcular_valor_consumo(30,69))