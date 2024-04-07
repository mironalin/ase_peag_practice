import numpy as np
import matplotlib.pyplot as graph

def ofTSP(perm, cost, length):
    value = 0
    for i in range(length - 1):
        value += cost[perm[i]][perm[i + 1]]
    
    value += cost[perm[0]][perm[length - 1]]
    return 100 / value    
    
def graph_rep(val, dim, n):
    x = [i for i in range(dim)]
    y = [val[i] for i in range(dim)]
    graph.plot(x, y, "gs-", markersize=11)
    graph.show()
    
def gen(file_cost, dim):
    cost = np.genfromtxt(file_cost)
    length = len(cost)
    
    pop = np.zeros((dim, length), dtype=int)
    value = np.zeros(dim, dtype=float)
    
    for i in range(dim):
        pop[i] = np.random.permutation(length)
        value[i] = ofTSP(pop[i, :length], cost, length)
    
    graph_rep(value, dim, length)
    return [pop, value]
print(gen("/home/alinmiron/VsCodeProjects/ase_peag/Labs/labs_04/TSP/costuri.txt", 30))