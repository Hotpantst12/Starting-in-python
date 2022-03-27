

# programa notasFUNAR

nota1 = float(input('digite la primera nota: '))

nota2 = float(input('digite la segunda nota: '))

nota3 = float(input('digite la tercera nota: '))

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 3:
    print('aprovaste la materia. ')

if promedio>= 4:
    print('aprobo, felicidades. ') 

else:
    print('lo lamento, reprobo. ')


