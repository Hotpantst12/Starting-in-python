

'''calculadora de IMC'''

#IMC = Peso / (altura x altura)

# < 19 = delgadez

#entre 20 y 25 es peso normal

# de 26 a 30 seria sobrepeso

# mas de 30 es obesidad

def imc (speso , salturam):
    # salturam = alturam97

    # speso = peso
    IMS = speso / salturam
    return IMS


peso = int(input('Ingrese su peso actual en KG: '))

altura = int(input('ingrese su altura en cm: '))

alturam = (altura / 100) **2

#speso = ()

#salturam = ()

imc_v = int(imc(peso,alturam))

if imc_v <= 19:
    print(f'actualmente te encuentras delgado. ')

if (imc_v >= 20) and (imc_v <= 26):
    print(f'actualmente te encuentras en un peso normal. ')

if (imc_v >= 26) and (imc_v <= 30):
    print(f'actualmente te encuentras en el rango de sobrepeso. ')

if imc_v >= 30:
    print(f'actualmente te encuentras en el rango de obesidad. ')

