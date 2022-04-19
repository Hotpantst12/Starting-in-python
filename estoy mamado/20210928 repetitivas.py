def f_factorial(n:int)->int:
    f=1
    i=1
    while(i<=n):
        f=f*i
        i=i+1
    return f

def contar_digitos (n:int)->int:
    c=0
    while(n>0):
        n = n // 10
        c=c+1
    return c

"""
nombre
que hace
parametros
retorno
observacion:
a menor o igual a b
"""
def sumatoria_uno(a:int,b:int)->float:
    s = 0
    i= a
    while(i<=b):
        if (i==-4):
            e=0
        else:
            e= (i*i*i)/(i+4)
        s = s + e
        i=i+1
    return s

def sumatoria_dos(b:int)->float:
    s = 0
    k= 0
    while(k<=b):
        e= (k*k*k)/(k+4)
        s = s + e
        k=k+1
    return s

#codigo de prueba
#print("el factorial de 2000 tiene",contar_digitos( f_factorial(2000) )," digitos")
#print("sumatoria dio ",sumatoria_uno(-10,5))
print("sumatoria dio ",sumatoria_uno(3,5))
