    #un empleado trabaja 40 horas semanales en una empresa y recibe un salario de 260.000 pesos semanales.
    #Si excede de las 40 horas la empresa debe pagar un recargo del 30% por hora extra trabajadas Hacer una función que, 
    #dadas las horas semanales trabajadas de un empleado, retorne el salario a pagar    

Limite_Semana_Horas = int(40)
Salario_Semana = int(260000)
HorasTrabajadas = int(input("Ingrese las horas trabajadas: "))
ValorHora = int(Salario_Semana / 40)
def HorasExtras(HorasTrabajadas):
    HorasTrabajadas-40
    return     
def SalarioSemanalFijo():
    SalarioSemanalFijo = ValorHora*40
    return SalarioSemanalFijo
def SalarioSemanalPorHoras():
    SalarioSemanal = ValorHora*HorasTrabajadas
    return SalarioSemanal
def Recargo(HorasTrabajadas):
    recargo = HorasTrabajadas-40
    ValorHoraRecargo = recargo*ValorHora*1.3
    return ValorHoraRecargo

if HorasTrabajadas > Limite_Semana_Horas:
    print("#######################")
    print("Usted aplica a recargo, usted ha trabajado mas de 40 horas")
    print("Sus horas trabajadas fueron: ",HorasTrabajadas)
    print("#######################")
    total = int(Salario_Semana+Recargo(HorasTrabajadas))
    print("Su salario es :",total,"COP")

else:
    print("Su salario es:",SalarioSemanalPorHoras(),"COP")


