# Scrieți o funcție Python care generează o matrice cu 10 linii vectori cu 8 elemente: 7 biți reprezentând
# un individ și un număr întreg reprezentând calitatea acestuia. Calitatea unui individ este dată de
# numărul de biți 1 din pozițiile impare – prima poziție în vector este considerată număr impar. (de
# exemplu, calitatea lui [1,0,0,1,1,0,1] = 3). Calculați și afișați calitatea medie a celor 10 indivizi.

import numpy as np

def calculate_quality(ind):
    quality = sum(ind[i] for i in range(0, len(ind), 2))
    return quality

def gen(dim):
    inds = []
    
    for i in range(dim):
        ind = np.random.randint(2, size=8)
        quality = calculate_quality(ind)
        inds.append((ind, quality))
        
    return inds

def calculate_avg_quality(inds):
    total_quality = sum(quality for i, quality in inds)
    avg_quality = total_quality / len(inds)
    return avg_quality

inds = gen(10)
avg_quality = calculate_avg_quality(inds)

print(f"\nAverage quality of the {len(inds)} individuals: {avg_quality}")