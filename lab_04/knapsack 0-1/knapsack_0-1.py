import numpy as np
import matplotlib.pyplot as graph

def read_from_file(file_name):
    return np.genfromtxt(file_name) 


def check_ok(x, n, c, v, max):
    value = 0
    cost = 0
    for i in range(n):
        value += x[i] * v[i]
        cost += x[i] * c[i]
    return cost <= max, value

def graphic_rep(pop, dim, n):
    x = [i for i in range(dim)]
    y = [pop[i][n] for i in range(dim)]
    
    graph.plot(x, y, "gs-", markersize = 11)
    graph.show()

def generate(file_cost, file_value, max, dim):
    cost_list = read_from_file(file_cost)
    value_list = read_from_file(file_value)
    
    n = len(cost_list)
    pop = []
    
    for i in range(dim):
        found = False
        
        while not found:
            x = np.random.randint(0, 2, n)
            found, value = check_ok(x, n, cost_list, value_list, max)
    
        x = list(x)
        x += [value]
        pop += [x]

    graphic_rep(pop, dim, n)
    return pop


# print(read_from_file("valoare.txt")[3])
print(generate("cost.txt", "valoare.txt", 50, 100))