import numpy as np
import matplotlib.pyplot as graph

def check_ok(x, n, c, v, max):
    val = 0
    cost = 0
    for i in range(n):
        val += x[i] * v[i]
        cost += x[i] * c[i]
    
    return cost <= max, val

def graphic_rep(pop, dim, n):
    x = [i for i in range(dim)]
    y = [pop[i][n] for i in range(dim)]
    
    graph.plot(x, y, "gs-", markersize = 11)
    graph.show()


def gen(file_cost, file_value, max, dim):
    cost = np.genfromtxt(file_cost)
    value = np.genfromtxt(file_value)
    
    length = len(cost)
    pop = []
    
    for i in range(dim):
        found = False
        
        while not found:
            x = np.random.uniform(0, 1, length)
            found, val = check_ok(x, length, cost, value, max)
        
        x = list(x)
        x += [val]
        pop += [x]
    
    graphic_rep(pop, dim, length)
    return pop
    
print(gen("cost.txt","valoare.txt",30,10))