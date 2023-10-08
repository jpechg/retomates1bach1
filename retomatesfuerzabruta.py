import itertools
from tqdm import tqdm
def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key

# Generar todas las posibles combinaciones de 5 números del 1 al 49
combinaciones = list(itertools.combinations(range(1, 50), 5))

total_combinaciones = len(combinaciones)

# Caso a) Adivinar todos los números correctamente
# Solo hay una combinación ganadora, por lo que la probabilidad es 1 / total_combinaciones
prob_a = 1 / total_combinaciones
'''
# Caso b) 2 números en el mismo lugar de las decenas y los otros 3 números en diferentes lugares de las decenas
conteo_b = 0
i=0
for combinacion in tqdm(combinaciones):
    decenas = [numero // 10 for numero in combinacion]
    #print(combinacion)
    if len(set(decenas)) == 4 and decenas.count(max(decenas, key=decenas.count)) == 2:
        conteo_b += 1
        #if i%413 == 0:
            #print(combinacion)
        #i = i + 1
print(conteo_b)
prob_b = conteo_b / total_combinaciones
'''
# Caso c) Solo 2 números que tienen el mismo lugar
conteo_c = 0
i = 0
for combinacion in combinaciones:

    unidades = [numero % 10 for numero in combinacion]

    if len(set(unidades)) == 4 and unidades.count(max(unidades, key=unidades.count)) == 2:
        conteo_c += 1
        if i%1 == 0:
            print(combinacion)
        i = i + 1

print(conteo_c)        
prob_c = conteo_c / total_combinaciones

def testJuan (combinacion):
    unidades = [numero % 10 for numero in combinacion]
    print(unidades)
    print(len(set(unidades)))
    print(unidades.count(max(unidades, key=unidades.count)))

    if len(set(unidades)) == 4 and unidades.count(max(unidades, key=unidades.count)) == 2:
        print("hola")
    else:
        print("estaba bien!")
    print(unidades)
    


testJuan([1,11,23,33,45])


'''
print(combinaciones[0])
print(combinaciones[len(combinaciones)-1])
'''
print(f"Probabilidad de acertar los 5 números correctamente: {prob_a}")
#print(f"Probabilidad de Que 2 números estén en la misma decena y los otros 3 en decenas distintas: {conteo_b}/{total_combinaciones}")
print(f"Probabilidad de solo 2 números tengan la misma unidad: {conteo_c}/{total_combinaciones}")

