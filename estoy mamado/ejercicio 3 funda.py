
# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra

#calcular f(x)
import math
variable:float
variable = float(input('digite el valor de la variable'))
if variable <= 5:
    variable=variable
    print ('el valor de la variable segun la funcoion es: ')
    print(variable)
elif variable >=-5 and variable>=5:
    variable=variable+3
    print('el valor de la variable segun la fincion: ')
elif variable>5:
    variable=math.pow(variable, 2)-2
    print('el valor de la variable segun la funcion es: ')
    print(variable)
else:
    print('hubo un error')


