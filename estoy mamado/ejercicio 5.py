

# escriba una funcion con 2 parametros de tal forma que determine si estos dos son multiplos entre si
# esta funcion debe retornar true si son multiplos
# y false si no son (3.6)

def multiplos (x,y):
    return True if x / y == 0 else False
print(multiplos (6,3))