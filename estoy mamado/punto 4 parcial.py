

def calcular_nota_final (nota1,nota2,nota3):
    if nota1 > 3.5:
        return nota1 + 0.4
    elif nota2 < 2.5:
        return nota2 - 0.3
    elif nota3 < 0:
        return nota3 == 0
    
print (calcular_nota_final(3.5 , 2.9 , 4.0))