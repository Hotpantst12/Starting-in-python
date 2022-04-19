
# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra




def tipo_triangulo(num1, num2,num3):
    if num1 == num2 and num2 == num3:
        return 'equilatero'
    elif num1==num3:
        return 'isosceles'
    else:
        return 'escaleno'
