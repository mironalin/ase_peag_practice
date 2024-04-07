# Scrieți o funcție Python care generează o matrice cu n linii, fiecare linie conținând o permutare de
# dimensiune 8 (n parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune 8) este dată de numărul perechilor (i,j), i<j, pentru care P(i)=j și
# P(j)=i. Evaluați cei n indivizi generați și afișați valoarea maximă a calității.

import numpy as np

def calculate_quality(perm):
    quality = 0
    
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if perm[i] == j and perm[j] == i:
                quality += 1
                
    return quality

def gen(dim):
    perms = []
    
    for i in range(dim):
        perm = np.random.permutation(8)
        quality = calculate_quality(perm)
        perms.append((perm, quality))
        
    return perms

def find_max_quality(perms):
    max_quality = max(perms, key = lambda x: x[1])[1]
    return max_quality

perms = gen(15)
max_quality = find_max_quality(perms)

print("\nPermutations and the qualities:")
for i, (perm, quality) in enumerate(perms):
    print(f"Permutation {i + 1}: {perm} - Quality: {quality}")
    
print(f"\nMaximum quality found: {max_quality}")