# Scrieți o funcție Python care generează o matrice cu 15 linii, fiecare linie conținând o permutare de
# dimensiune k (k parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune k) este dată de numărul perechilor (i,j), i<j, pentru care P(i)-
# P(j)=număr par. Evaluați cei 15 indivizi generați și afișați valoarea maximă.

import numpy as np

def calculate_quality(perm):
    quality = 0
    for i in range(len(perm)):
        for j in range(i + 1, len(perm)):
            if (perm[i] - perm[j]) % 2 == 0:
                quality += 1
    
    return quality

def gen(k, dim):
    perms = []
    
    for i in range(dim):
        perm = np.random.permutation(k)
        quality = calculate_quality(perm)
        perms.append((perm, quality))
    
    return perms

def find_max_quality(perms):
    max_quality = max(perms, key = lambda x: x[1])[1]
    return max_quality

perms = gen(5, 15)
max_quality = find_max_quality(perms)

print("/nPermutations and their qualities:")
for i, (perm, quality) in enumerate(perms):
    print(f"Permutation {i + 1}: {perm} - Quality: {quality}")
    
print("\nMaximum quality found: ", max_quality)