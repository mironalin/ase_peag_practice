# Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând: a) o permutare P
# de dimensiune k (k parametru de intrare), cu proprietatea că P(1)=1 și P(k)=k; b) o valoare care
# reprezintă calitatea permutării. Calitatea unui individ P (permutare de dimensiune k) este dată de
# numărul de elemente i cu proprietatea că P(i)<i. Evaluați cei 10 indivizi generați și afișați valoarea
# maximă

import numpy as np

def calculate_quality(perm):
    quality = sum(1 for i in range(len(perm)) if perm[i] < i + 1)
    return quality

def gen(k, dim):
    perms = []
    
    for i in range(dim):
        perm = np.random.permutation(k) + 1
        perm[0], perm[-1] = 1, k
        quality = calculate_quality(perm)
        perms.append((perm, quality))
    
    return perms

def find_max_quality(perms):
    max_quality = max(perms, key=lambda x: x[1])[1]
    return max_quality

perms = gen(8, 10)

print("\nPermutations and their qualities:")
for i, (perm, q) in enumerate(perms):
    print(f"Permutation {i+1}: {perm} - Quality: {q}")

# Găsim și afișăm valoarea maximă a calității
max_quality = find_max_quality(perms)
print("\nMaximum quality found:", max_quality)