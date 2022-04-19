def calcular_pago_secuencial(minutos:int)->int:
    if (minutos<=15):
        total=500
        
    if ((minutos>15) and (minutos<=30)):
        total=1000
        
    if ((minutos>30) and (minutos<=60)):
        total=1400
        
    if (minutos>60):
        extras=minutos-60
        total=1400 +(extras*20)      
    return total



def calcular_pago(minutos:int)->int:
    if (minutos<=15):
        total=500
    else:
        if (minutos<=30):
            total=1000
        else:
            if (minutos<=60):
                total=1400
            else:
                extras=minutos-60
                total=1400 +(extras*20)
    return total

def tipo_triangulo(a:int,b:int,c:int)->str:
    rta:str
    if ((a==b)and(a==c)):
        rta="Equilatero"
    else:
        if ((a==b)or(a==c)or(b==c)):
            rta="Isoceles"
        else:
            rta="Escaleno"
    return rta


#codigo de prueba
print("tiene que pagar dio:",calcular_pago_secuencial(62))
print("tipo de trigulo:",tipo_triangulo(2,2,20))
