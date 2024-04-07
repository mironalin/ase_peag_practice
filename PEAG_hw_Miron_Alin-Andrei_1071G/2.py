# Scrieți o funcție Python care generează o matrice (populație) cu 18 linii vectori cu 6 elemente: 5 biți
# reprezentând un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui individ este
# dată de numărul perechilor de valori consecutive diferite (de exemplu, calitatea lui [1,0,0,1,1] = 2).
# Calculați și afișați indivizii cu cea mai mare valoare a funcției calitate.

import numpy as np

def calculate_quality(individual):
    quality = np.sum(individual[: -1] != individual[1:])
    return quality

def generate_population(rows, columns):
    pop = []
    
    for i in range(rows):
        individual = np.random.randint(0, 2, size = columns)
        quality = calculate_quality(individual)
        pop.append((individual, quality))
    return pop

def get_highest_quality_individuals(pop):
    max_quality = max(pop, key = lambda x: x[1])[1]
    return [individual for individual, quality in pop if quality == max_quality]

pop = generate_population(18, 5)
print("Population:")
for individual, quality in pop:
    print(f"Individual: {individual} Quality: {quality}")
    
highest_quality_individuals = get_highest_quality_individuals(pop)
print("\n Individuals with highest quality:")
for individual in highest_quality_individuals:
    print(f"Individual: {individual}")