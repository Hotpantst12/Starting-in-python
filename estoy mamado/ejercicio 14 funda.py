
# David Ricardo Carvajal Rincon
# Belen nathalia pedraza becerra

def calcular_valor_pagar(num1,x):
    if num1>=0 and num1<=2 and x=='normal':
         return 500*num1
    elif num1>=0 and num1<=2 and x=='especial':
         return 450*num1
    elif num1>2 and x=='normal':
         return 300*num1
    elif num1>2 and x=='especial':
         return 250*num1