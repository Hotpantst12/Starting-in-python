

'''monda de la formula cuadratica'''


a = int(input('introduzca el valor de a: '))

b = int(input('introduzca el valor de b: '))

c = int(input('introduzca el valor de c: '))

formula = - b + (((b ** 2)- (4 * a * c)**0.5)/(2*a))

formula2 = - b - (((b ** 2)- (4 * a * c)**0.5)/(2*a))

print('el resultado es: ' + repr(formula))

print('el resultado es: ' + repr(formula2))

