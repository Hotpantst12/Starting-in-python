#sum_pares(247)
from configparser import SafeConfigParser
import math
a,b,c,d,f,g,par,impar=int
par=0
impar=0
print("Digite un numero de tres cifras: ")
b=a/100
c=a/10
d= a*0.10
c= c*0.10
e= b*0.02
f= c*0.02
g=d*0.02
if (e==0):
    par=par+b
else:
     impar=impar+b
if (f==0):
    par=par+c
else:
    impar=impar+c
if(g==0):
    par=par+d
else:
    impar=impar+d
print(f"La suma de los pares es: {par}")
print(f"La suma de los impares es: {impar}")