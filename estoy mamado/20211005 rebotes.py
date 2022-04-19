"""
---------------
contar_rebotes
---------------
autor: Luis Alberto Esteban
cuenta los rebotes de una pelota soltada desde una altura dada
parametros:
    un numero real positivo "altura_inicial" que representa la altura desde donde se suelta la pelota
    un numero real positivo "hasta" que representa la altura hasta donde se desean contar los rebotes
retorna:
    un entero positivo que representa el numero de rebotes
Ejemplos:
   contar_rebotes(100,0.5) retorna 51 
   contar_rebotes (40,10) retorna 14 
"""

def contar_rebotes(altura_inicial:int, hasta:int)->int:
    altura_actual=altura_inicial
    rebotes=0
    while(altura_actual>=hasta):
         altura_actual=altura_actual - (altura_actual*10)/100
         rebotes=rebotes +1
    return rebotes

"""
---------------
contar_dias
---------------
autor: Luis Alberto Esteban
cuenta los dias necesarios para alcanzar un saldo final a partir de un saldo incial
parametros:
    un numero real positivo "saldo_inicial" que representa la el dinero con el cual se abre la cuenta
    un numero real positivo "saldo_final" que representa la dinero al cual desea llegar 
retorna:
    un entero positivo que representa el numero de dias necesarios para llegar el saldo final segun condiciones del banco
Ejemplos:
   contar_dias(450000, 1200000) retorna 392
"""
def contar_dias(saldo_inicial:float, saldo_final:float)->int:
    saldo_actual=saldo_inicial
    dias=0
    while(saldo_actual<=saldo_final):
        if(saldo_actual<=500000):
            p_interes=0.2
        if ((saldo_actual>500000) and (saldo_actual<=1000000)):
            p_interes=0.25
        if (saldo_actual>1000000):
            p_interes=0.3
        saldo_actual=saldo_actual +  (p_interes*saldo_actual)/100
        dias=dias +1
    return dias

    
def contar_dias_2(saldo_inicial:float, saldo_final:float)->int:
    saldo_actual=saldo_inicial
    dias=0
    while(saldo_actual<=saldo_final):
        if(saldo_actual<=500000):
            p_interes=0.2
        else:
            if (saldo_actual<=1000000):
                p_interes=0.25
            else:
                p_interes=0.3
        saldo_actual=saldo_actual +  (p_interes*saldo_actual)/100
        dias=dias +1
    return dias



def calcular_saldo_despues_de(saldo_inicial:float, n_dias:int)->float:
    saldo_actual=saldo_inicial
    dia=1
    while(dia<=n_dias):
        if(saldo_actual<=500000):
            p_interes=0.2
        else:
            if (saldo_actual<=1000000):
                p_interes=0.25
            else:
                p_interes=0.3
        saldo_actual = saldo_actual +  (p_interes*saldo_actual)/100
        dia=dia +1
    return saldo_actual

"""
Diseño estructurado
Un solo ejercicio

total_pagar

p_descuento_motivo
p_descuento_cantidad
valor_individual


"""
def p_descuento_motivo(motivo:str)->float:
    if (motivo=="Negocios"):
        rta=0
    else:
        if (motivo=="Familiar"):
            rta=7
        else:
            if (motivo=="Turismo"):
                rta=4.75
            else:
                rta=0
    return rta

"""
          0  
3 – 5     2,6
6 – 10    5,38
11 y más  7,24
"""
def p_descuento_cantidad(n_tiquetes:int)->float:
    if(n_tiquetes<3):
        rta=0
    else:
        if(n_tiquetes<=5):
            rta=2.6
        else:
            if(n_tiquetes<=10):
                rta=5.38
            else:
                rta=7.24
    return rta

"""
Destinos
         Miami  Madrid
Clases
Primera 1300000 2700000
Segunda 1120000 2500000
Tercera 1100000 2320000
"""
def valor_individual(destino:str,clase:int)->float:
    if(destino=="Miami"):
        if(clase==1):
            valor=1300000
        else:
            if(clase==2):
                valor=1120000
            else:
                valor=1100000
    else:
        if(clase==1):
            valor=2700000
        else:
            if(clase==2):
                valor=2500000
            else:
                valor=2320000
    return valor

def total_pagar (d:str, c:int, m:str, n:int)->float:
    x=valor_individual(d,c)
    p1=p_descuento_cantidad(n)
    p2=p_descuento_motivo(m)
    pt=p1+p2
    subtotal=x*n
    total=subtotal - (pt*subtotal)/100
    return total

#codigo prueba

print(total_pagar("Miami",1,"Negocios",1))


