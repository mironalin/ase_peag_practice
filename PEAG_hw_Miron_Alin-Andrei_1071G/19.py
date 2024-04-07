# Scrieți o funcție Python care generează o matrice cu n linii (n parametru de intrare), fiecare linie
# conținând: a) o permutare de dimensiune 6 în care valoarea 1 nu apare în prima jumătate; b) o valoare
# care reprezintă calitatea permutării. Calitatea unui individ P (permutare de dimensiune 6) este dată
# de suma pozițiilor pe care apar valorile pare (de exemplu, individul P=[2,5,4,3,0,1] este fezabil pentru
# că 1 apare în ultima poziție; calitatea lui P este 0+2+4=6). Evaluați cei n indivizi generați și afișați
# valoarea maximă a calității.

import numpy as np

def calculate_quality(perm):
    quality = sum(i for i, x in enumerate(perm) if x % 2 == 0)
    return quality

def gen(dim):
    perms = []
    for i in range(dim):
        perm = np.random.permutation(6)
        
        while perm[0] < 2 or perm[1] < 2 or perm[2] < 2:
            perm = np.random.permutation(6)
        
        quality = calculate_quality(perm)
        perms.append((perm, quality))
        
    return perms

def find_max_quality(perms):
    max_quality = max(perms, key=lambda x: x[1])[1]
    return max_quality

perms = gen(10)

print("\nPermutations and their qualities:")
for i, (perm, q) in enumerate(perms):
    print(f"Permutation {i + 1}: {perm} - Quality: {q}")
    
max_quality = find_max_quality(perms)
print(f"\nMaximum quality found: {max_quality}")