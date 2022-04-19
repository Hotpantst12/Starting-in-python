

# calcular el valor absoluto de un numero real, sin usar funciones. 

# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra



def valor_absoluto (numero):
    if (numero <= 0):
        numero = numero * (-1)
    else:
        numero = numero
    return  numero 

numero = float (input('Digite su numero: '))
print(valor_absoluto(numero))
