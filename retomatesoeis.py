import itertools

def c(n,k):

    #print(f"elementos: {i+1}")

    combinaciones = list(itertools.combinations(range(1, n+1), k))

    conteo_c = 0

    for combinacion in combinaciones:

        unidades = [numero % 10 for numero in combinacion]
        if len(set(unidades)) == 4 and unidades.count(max(unidades, key=unidades.count)) == 2:
            conteo_c += 1   
    return(conteo_c)

for i in range(1, 25):
    print(c(i,5))