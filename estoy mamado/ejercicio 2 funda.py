
# Realizar dos funciones que encuentren el número mayor y la otra el número menor de 3

# números dados como parámetros a la respectiva función de tal forma que  mayor(3,7,9)

# retornará 9  y menor(7,9,3) retornará 3

# David Ricardo Carvajal Rincon

# Belen nathalia pedraza becerra

def numero_mayor (n1 , n2 , n3):
    if (n1 > n2) and (n2 > n3):
        return n1
    elif (n2 > n1 ) and (n2 > n3):
        return n2
    else:
        return n3
def numero_menor (n1, n2 , n3):
    if (n1 < n2) and (n2 > n3):
        return n3
    elif (n2 < n1) and (n2 > n3):
        return n2
    else:
        return n1
    
n1 = int (input('digite el primer numero: '))
n2 = int (input('digite el segundo numero: '))
n3 = int(input('digite el tercer numero: '))

print (numero_mayor(n1, n2 , n3))
print (numero_menor (n1, n2 , n3))


