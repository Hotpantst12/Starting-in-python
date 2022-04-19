total:int
valorkilo:int
def totalpagarlavanderia (tipocliente,pesoropa):
    if tipocliente == 'normal':
        if pesoropa <= 2:
            valorkilo = 200
        else:
            valorkilo= 500
    else:
        if pesoropa <= 2:
            valorkilo=150
        else:
            valorkilo=450
    return pesoropa*valorkilo

t:int

t = totalpagarlavanderia('normal', 2)

print(t)


