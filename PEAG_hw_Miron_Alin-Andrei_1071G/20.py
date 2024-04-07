# Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând 7 valori: a) un
# individ vector de dimensiune 6, cu elemente numere întregi din mulțimea {−2, −1,0,1,2,3,4} și cu
# proprietatea că suma elementelor este mai mică decât 10; b) calitatea individului. Calitatea unui
# individ este dată de produsul valorilor absolute ale elementelor sale. Afișați indivizii generați în
# ordinea inversă a calităților.

import numpy as np

def calculate_quality(ind):
    quality = np.prod(np.abs(ind))
    return quality

def gen(dim):
    inds = []
    
    for i in range(dim):
        while True:
            ind = np.random.randint(-2, 5, size = 6)
            if sum(ind) < 10:
                break
        
        quality = calculate_quality(ind)
        inds.append((ind, quality))
    
    return inds

def display(inds):
    sorted_inds = sorted(inds, key=lambda x: x[1], reverse=True)
    print("\nGenerated individuals in descending order of their qualities:")
    for i, (ind, q) in enumerate(sorted_inds):
        print(f"Individual {i+1}: {ind} - Quality: {q}")

inds = gen(10)

display(inds)