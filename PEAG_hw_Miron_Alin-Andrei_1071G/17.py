# Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând k+1 valori (k
# parametru dat): a) un individ vector de dimensiune k, cu elemente numere întregi din mulțimea
# {1,2,3,4,5,6} și cu proprietatea că în ultima poziție valoarea este număr par; b) calitatea individului.
# Calitatea unui individ este dată de produsul elementelor sale. Afișați indivizii generați în ordinea
# crescătoare a calităților.

import numpy as np

def calculate_quality(ind):
    quality = np.prod(ind)
    return quality

def generate_individuals(n, k):
    inds = []
    for i in range(n):
        ind = np.random.choice([1, 2, 3, 4, 5, 6], size=k)
        if ind[-1] % 2 != 0:
            ind[-1] += 1
        quality = calculate_quality(ind)
        inds.append((ind, quality))
    return inds

def display(inds):
    sorted_inds = sorted(inds, key=lambda x: x[1])
    print("\nGenerated individuals in increasing order of their qualities:")
    for i, (ind, quality) in enumerate(sorted_inds):
        print(f"Individual {i+1}: {ind} - Quality: {quality}")

inds = generate_individuals(10, 5)

display(inds)
