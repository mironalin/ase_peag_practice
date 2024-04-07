# Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând un individ vector binar de dimensiune 8, cu număr impar de biți 1 și calitatea asociată
# șirului. Calitatea unui individ este dată de valoarea în bază 10 a reprezentării binare (individul [0 0 0 0
# 0 0 1 1] are calitatea 3). Calculați și afișați indivizii cei mai buni (cu calitatea maximă).

import numpy as np

def calculate_quality(individual):
    decimal_value = int(''.join(map(str, individual)), 2)
    return decimal_value

def gen(dim):
    individuals = []
    
    for i in range(dim):
        individual = np.random.choice([0, 1], size = 8)
        
        while np.sum(individual) % 2 != 1:
            individual = np.random.choice([0, 1], size = 8)
        
        quality = calculate_quality(individual)
        individuals.append((individual,quality))
        
    return individuals

def find_best_individuals(individuals):
    max_quality = max(individuals, key = lambda x: x[1])[1]
    best_individuals = [i for i, q in individuals if q == max_quality]
    return best_individuals

individuals = gen(15)
best_individuals = find_best_individuals(individuals)

print("\nGenerated individuals and their qualities:")
for i, (individual, quality) in enumerate(individuals):
    print(f"Individual {i + 1}: {individual} - Quality: {quality}")
    
print("\nBest individual:")
for i, individual in enumerate(best_individuals):
    print(f"Best individual {i + 1}: {individual}")