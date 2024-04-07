import numpy as np
from math import sin, cos
import matplotlib.pyplot as graph

def f_objective(x):
    y = x**3 * sin(x/3) + x**3 * cos(2*x) -x*sin(3*x) + x*cos(x)
    
    return y

def neighbours(x, no, dist, a, b):
    neighbours = [x + i * dist for i in range(-no, no + 1) if ((x + i * dist >=a) and (x + i * dist <= b))]
    val_neighbours = [f_objective(x + i * dist) for i in range(-no, no + 1) if ((x + i * dist >=a) and (x + i * dist <= b))]
    
    return [neighbours, val_neighbours]
    
def HC(a, b, no_of_points, no_of_neigbours, dist):
    X = [None] * no_of_points
    Y = [None] * no_of_points
    
    for i in range(no_of_points):
        start_point = np.random.uniform(a, b)
        local_point = 0
        
        while not local_point:
            n_neighb, n_values = neighbours(start_point, no_of_neigbours, dist, a, b)
            max_value = max(n_values)
            pos = n_values.index(max_value)
            max_neighb = n_neighb[pos]
            
            if max_value > f_objective(start_point):
                start_point = max_neighb
            else:
                local_point = 1
        
        X[i] = max_neighb
        Y[i] = f_objective(max_neighb)
        
    fx = max(Y)
    pos = Y.index(fx)
    x = X[pos]
    
    print("Calculated maximum value/Valoare maxima calculata: ", fx)
    print("It's at the point/E atinsa in punctul: ", x)
    show_graph(a, b, X, Y, x, fx)
    return [x, fx]
    
    
def show_graph(a, b, X, Y, x_max, y_max):
    x = np.arange(a, b, 0.01)
    graph.plot(x, [f_objective(i) for i in x], "k-", X, Y, "bo", x_max, y_max, "r*", markersize = 10)
    graph.show()


print(HC(-3, 25, 100, 5, 0.1))