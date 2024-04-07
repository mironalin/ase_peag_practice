# Scrieți o funcție Python care generează o matrice cu 10 linii vectori cu k+1 elemente (k parametru
# dat): k biți reprezentând un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui
# individ este dată de numărul perechilor de valori consecutive egale. (de exemplu, pentru k=5, calitatea
# lui [0,0,0,1,1] = 3). Afișați indivizii generați în ordinea crescătoare a calităților lor.

import numpy as np

def calculate_quality(ind):
    quality = 0
    
    for i in range(len(ind) - 1):
        if ind[i] == ind[i + 1]:
            quality += 1
            
    return quality

def gen(dim, k):
    inds = []
    
    for i in range(dim):
        ind = np.random.randint(2, size=k)
        quality = calculate_quality(ind)
        inds.append((ind, quality))
        
    return inds

def display(inds):
    sorted_inds = sorted(inds, key=lambda x:x[1])
    print("\nGenerated individuals in increasing order of their qualities")
    for i, (ind, q) in enumerate(sorted_inds):
        print(f"Individual {i + 1}: {ind} - Quality: {q}")
        
inds = gen(10, 5)
display(inds)