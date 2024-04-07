# Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând 9 valori: a) un individ vector de dimensiune 8, cu elemente numere întregi din mulțimea
# {1,2,3,4} și cu proprietatea că în poziția a 5-a valoarea este număr impar; b) calitatea individului.
# Calitatea unui individ este dată de produsul elementelor sale. Calculați și afișați indivizii cei mai slabi
# (cu calitatea minimă).

import numpy as np

def calculate_quality(individual):
    return np.prod(individual)
    
def gen(dim):
    individuals = []
    
    for i in range(dim):
        individual = np.random.choice([1, 2, 3, 4], size = 8)
        individual[4] = np.random.choice([1, 3])
        quality = calculate_quality(individual)
        individuals.append((individual, quality))
        
    return individuals

def find_min_quality_individuals(individuals):
    min_quality = min(individuals, key = lambda x: x[1])[1]
    min_quality_individuals = [i for i, q in individuals if q == min_quality]
    return min_quality_individuals

individuals = gen(15)
min_quality_individuals = find_min_quality_individuals(individuals)

print("\nGenerated individuals and their qualities:")
for i, (individual, quality) in enumerate(individuals):
    print(f"Individual {i + 1}: {individual} - Quality: {quality}")
    
print("\nMin quality individuals:")
for i, individual in enumerate(min_quality_individuals):
    print(f"Min quality Individual {i + 1}: {individual}")