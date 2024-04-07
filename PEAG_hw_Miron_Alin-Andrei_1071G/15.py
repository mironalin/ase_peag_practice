# Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând 10 elemente: un individ vector binar de dimensiune 9, cu 5 biți egali cu 1 și calitatea asociată
# șirului. Calitatea unui individ este dată de suma pozițiilor care conțin 1. Prima poziție este 0 (de
# exemplu individul [1 0 0 0 1 0 1 1 1] are calitatea 25). Calculați și afișați indivizii generați, împreună cu
# calitățile lor.

import numpy as np

def calculate_quality(ind):
    quality = np.sum(ind * np.arange(len(ind)))
    return quality

def gen(dim):
    inds = []
    
    for i in range(dim):
        ind = np.zeros(9, dtype=int)
        indices = np.random.choice(9, 5, replace=False)
        ind[indices] = 1
        quality = calculate_quality(ind)
        inds.append((ind, quality))
        
    return inds

inds = gen(10)

print("Generated individuals and their qualities:")
for i, (individual, quality) in enumerate(inds):
    print(f"Individual {i+1}: {individual} - Quality: {quality}")
