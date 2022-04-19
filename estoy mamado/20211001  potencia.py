def potencia (base:float, exponente:int)->float:

    if (exponente<0):
        e= -1*exponente
    else:
        e= exponente
    
    rta=1
    i=1
    while(i<=e):
       rta= rta *base
       i=i+1

    if (exponente<0):
        rta= 1/rta
    return rta

def potencia_uno (base:float, exponente:int)->float:

    if (exponente<0):
        rta=1
        i=1
        while(i<=-1*exponente):
            rta= rta *base
            i=i+1
        rta=1/rta
        
    else:
        rta=1
        i=1
        while(i<=exponente):
            rta= rta *base
            i=i+1     
    return rta



def invertir_numero(n:int)->int:
    rta=0
    while(n>0):
       d = n % 10
       rta= rta*10 + d
       n = n // 10
    return rta

def palindromo(x:int)->bool:
    y=invertir_numero(x)
    if (x==y):
        rta=True
    else:
        rta=False
    return rta

def fibonacci(n:int)->int:
    a=1
    b=1
    c=1
    i=3
    while(i<=n):
         a=b
         b=c
         c=a+b
         i=i+1
    return c

    
def raiz_cuadrada(n:float)->float:
    a=n/2
    diferencia=10
    while(diferencia>0.0000000000000001):
        b=(a+(n/a))/2
        if (a>b):
            diferencia=a-b
        else:
            diferencia=b-a
        a=b
        
    return a

    
    

#codigo de prueba
#print(potencia(2,-3))
#print(potencia_uno(2,-3))
print(raiz_cuadrada(4.72))




