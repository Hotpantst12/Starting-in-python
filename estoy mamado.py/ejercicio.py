

numero1 = int(input('digite el primer numero: '))

numero2 = int(input('digite el segundo numero: '))

def sumar (pnum1  ,  pnum2):
    #numero1=num1
    #numero2=num2
    suma = pnum1 + pnum2
    return pnum1+pnum2 

def multiplicar (pnum1, pnum2):
    multiplicacion = pnum1 * pnum2  
    return pnum1*pnum2

def restar (pnum1, pnum2):
    resta = pnum1 - pnum2
    return pnum1-pnum2

def dividir(pnum1, pnum2):
    division = pnum1 / pnum2
    return pnum1/pnum2


def potenciar(pnum1, pnum2):
    potencia = pnum1 **2 , pnum2 **2
    return pnum1**2,pnum2**2
def modular(pnum1,pnum2):
    modulo = pnum1 % pnum2
    return pnum1 % pnum2

if numero1 > numero2:
    print(f'la suma es: {sumar(numero1, numero2)}')
    print(f'la multiplicacion es: {multiplicar(numero1,numero2)}')

if numero1 < numero2 :
    print(f'la resta es: {restar(numero1, numero2)}')
    print(f'la division es: {dividir(numero1, numero2)}')

if numero1 == numero2:
    print(f'la potencia es: {potenciar(numero1, numero2)}')
    print(f'el modulo es: {modular(numero1, numero2)}')

