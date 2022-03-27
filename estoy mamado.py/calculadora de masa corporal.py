

'''calculadora de IMC'''

#IMC = Peso / (altura x altura)

# < 19 = delgadez

#entre 20 y 25 es peso normal

# de 26 a 30 seria sobrepeso

# mas de 30 es obesidad

def imc (speso , salturam):
    IMC = speso / (salturam **2)
    return peso / (alturam **2)


peso = int(input('Ingrese su peso actual en KG: '))

altura = int(input('ingrese su altura en cm: '))

alturam = altura / 100



if imc == 19:
    print(f'actualmente te encuentras delgado: {imc(peso, alturam)}')

if imc == 20 or imc == 26:
    print(f'actualmente te encuentras en un peso normal: {imc(peso, alturam)}')

if imc == 26 or imc == 30:
    print(f'actualmente te encuentras en el rango de sobrepeso: {imc(peso, alturam)}')

if imc == 30:
    print(f'actualmente te encuentras en el rango de obesidad: {imc(peso, alturam)}')



