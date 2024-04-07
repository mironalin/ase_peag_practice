# Scrieți o funcție Python care generează o matrice cu 10 linii, fiecare linie conținând k+1 valori: a) un
# individ vector de dimensiune k, cu elemente numere întregi din mulțimea {−4, −3, −2, −1,1,2,3,4} și
# cu proprietatea că suma elementelor este pozitivă; b) calitatea individului. Calitatea unui individ este
# dată de suma modulelor elementelor sale (de exemplu, pentru k=3 și x=[2,4,-3], x este fezabil, pentru
# că suma elementelor sale este 3>0; calitatea lui x este 9). Calculați și afișați indivizii cei mai slabi (cu
# calitatea minimă).

import numpy as np

def calculate_quality(ind):
    return np.sum(np.abs(ind))

def gen(dim, k):
    inds = []
    
    for i in range(dim):
        ind = np.random.choice([-4, -3, -2, -1, 1, 1, 2, 3, 4], size = k)
        
        while np.sum(ind) <= 0:
            ind = np.random.choice([-4, -3, -2, -1, 1, 1, 2, 3, 4], size = k)

        quality = calculate_quality(ind)
        inds.append((ind, quality))
    
    return inds

def find_min_quality_inds(inds):
    min_q = min(inds, key=lambda x: x[1])[1]
    min_q_inds = [ind for ind, quality in inds if quality == min_q]
    return min_q_inds

inds = gen(10, 3)
min_q_inds = find_min_quality_inds(inds)

print("Generated individuals and their qualities:")
for i, (ind, q) in enumerate(inds):
    print(f"Individual {i+1}: {ind} - Quality: {q}")

print("\nMin quality individuals:")
for i, ind in enumerate(min_q_inds):
    print(f"Min quality Individual {i+1}: {ind}")