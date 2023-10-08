import itertools
from tqdm import tqdm

# Generar todas las posibles combinaciones de 5 números del 1 al 49
combinaciones = list(itertools.combinations(range(1, 50), 5))

total_combinaciones = len(combinaciones)

# Caso a) Adivinar todos los números correctamente
# Solo hay una combinación ganadora, por lo que la probabilidad es 1 / total_combinaciones
prob_a = 1 / total_combinaciones

# Caso b) 2 números en el mismo lugar de las decenas y los otros 3 números en diferentes lugares de las decenas
conteo_b = 0
for combinacion in tqdm(combinaciones, desc="Calculando escenario b"):
    decenas = [numero // 10 for numero in combinacion]
    if len(set(decenas)) == 4 and decenas.count(max(decenas, key=decenas.count)) == 2:
        conteo_b += 1
prob_b = conteo_b / total_combinaciones

# Caso c) Solo 2 números que tienen el mismo lugar
conteo_c = 0
for combinacion in tqdm(combinaciones, desc="Calculando escenario c"):
    unidades = [numero % 10 for numero in combinacion]
    if len(set(unidades)) == 4 and unidades.count(max(unidades, key=unidades.count)) == 2:
        conteo_c += 1
prob_c = conteo_c / total_combinaciones

print(f"Probabilidad de acertar los 5 números correctamente: {prob_a}")
print(f"Probabilidad de que 2 números estén en el mismo lugar de las decenas y los otros 3 números en lugares diferentes de las decenas: {prob_b}")
print(f"Probabilidad de que solo 2 números tengan la misma posición: {prob_c}")
