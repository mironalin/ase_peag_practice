import numpy as np
import matplotlib.pyplot as graph

def ofNq(x, n):
    # the objective function for the N-queens problem
    # I: x - the individual (permutation) evaluated(a), n - the dimension of the problem
    # O: c - quality (the number of pairs of queens which are not attacking each other)
    quality = n * (n - 1) / 2
    
    for i in range(n - 1):
        for j in range(i + 1, n):
            if abs(i - j) == abs(x[i] - x[j]):
                quality -= 1

    return quality

def graph_rep(pop, dim, n):
    x = [i for i in range(dim)]
    y = [pop[i][n] for i in range(dim)]
    
    graph.plot(x, y, "gs-", markersize = 11)
    graph.show()

def gen(n, dim):
    pop = np.zeros((dim, n + 1), dtype=int)
    for i in range(dim):
        pop[i, :n] = np.random.permutation(n)
        pop[i, n] = ofNq(pop[i, :], n)
    
    # graph_rep(pop, dim, n)
    return pop

print(gen(8, 30))
