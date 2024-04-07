# Scrieți o funcție Python care generează o matrice cu n linii, fiecare linie conținând o permutare de
# dimensiune 7 (n parametru de intrare) și o valoare care reprezintă calitatea permutării. Calitatea unui
# individ P (permutare de dimensiune 7) este dată de numărul perechilor (i,i+1), pentru care P(i)=i+1 și
# P(i+1)=i. Evaluați cei n indivizi generați și afișați valoarea maximă a calității

import numpy as np

def calculate_quality(perm):
    quality = sum(1 for i in range(len(perm) - 1) if perm[i] == i + 1 and perm[i + 1] == i)
    return quality

def gen(dim):
    perms = []
    
    for i in range(dim):
        perm = np.random.permutation(7) + 1
        quality = calculate_quality(perm)
        perms.append((perm, quality))
        
    return perms

def find_max_quality(permutations):
    max_quality = max(permutations, key=lambda x: x[1])[1]
    return max_quality

# Generăm permutările
perms = gen(10)

# Afișăm permutările și calitățile lor
print("\nPermutations and their qualities:")
for i, (perm, quality) in enumerate(perms):
    print(f"Permutation {i+1}: {perm} - Quality: {quality}")

# Găsim și afișăm valoarea maximă a calității
max_quality = find_max_quality(perms)
print("\nMaximum quality found:", max_quality)