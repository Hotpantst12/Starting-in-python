
def sonaptas(piezas):
    contador = 0
    cantidad = 0
    while contador < piezas:
        longitud = float(input('digite la longitud: '))
        if (longitud >=1.20) and (longitud <=1.30):
            print ('son aptas')
            cantidad+=1
        else: 
            print('no son aptas')
        contador+=1
    return cantidad
def run():
    print('programa fabrica')
    piezas = int (input('digite el numero de piezas: '))
    print(f'las piezas aptas son: {sonaptas(piezas)}',)
if __name__=='__main__':
    run()


