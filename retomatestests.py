numbers = list(range(1,50))

def ifunit(lista, unit):
    a = 0
    for i in lista:
        if i % 10 == unit:
            a = a + 1
    return(a)

def ifnotunit(lista,notunit):
    a = 0
    for i in lista:
        if i % 10 != notunit:
            a = a + 1
    lasti = i
    return(a)

numerators = [0,0,0,0,0]
denominators = [0]

for i in range(0,2):

    hasunit = ifunit(numbers, i)
    print(f"numeros con la unidad {i}: {hasunit}")
    numerators[i] = hasunit
    print(numerators)

for i in range(0,3):
    
    numerators[i+2] = 
