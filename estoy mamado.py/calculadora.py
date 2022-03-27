
'''programa de calculadora'''


#asignacion


def sumar (pnum1  ,  pnum2):
    #numero=num1
    #numero2=num2
    suma = pnum1 + pnum2
    return pnum1+pnum2 


def restar (pnum1, pnum2):
    resta = pnum1 - pnum2
    return pnum1-pnum2


def multiplicar (pnum1, pnum2):
    multiplicacion = pnum1 * pnum2  
    return pnum1*pnum2


def dividir(pnum1, pnum2):
    division = pnum1 / pnum2
    return pnum1/pnum2

    
print('calculadora')


#asignacion

numero = int(input('escribe el numero con el cual quiere realizar la operacion. '))


numero2 = int(input('escriba el segundo numero con el cual quiera realizar la operacion. '))

#opciones

print('- Para realizar una suma, escriba el numero 1')

print('- Para realizar una resta, escriba el numero 2')

print('- Para realizar una multiplicacion, escriba el numero 3')

print('- Para realizar una Division, escriba el numero 4')

operacion = int(input('Escriba el numero de la operacion que quiera realizar: '))

if operacion == 1:
    print(f'la suma es: {sumar(numero, numero2)}')

if operacion ==2:
    print(f'la resta es: {restar(numero, numero2)}')

if operacion ==3:
    print(f'la multiplicacion es: {multiplicar(numero,numero2)}')

if operacion==4:
    print(f'la division es: {dividir(numero, numero2)}')

else:
    print('operacion incorrecta, empieza de nuevo. ')








