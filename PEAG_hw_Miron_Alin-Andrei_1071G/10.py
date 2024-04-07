# Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓: {𝑥 = (𝑥1, … , 𝑥10) 𝑥𝑖 ∈ {−1,1}, 𝑥1 + ⋯ + 𝑥9 + 𝑥10 ≥ 0 } → ℝ
# 𝑓(𝑥) = 𝑎 ∙ 𝑥1 + ⋯ + 𝑎 ∙ 𝑥10
# unde 𝑎 este un parametru dat.
# Generați o populație cu n elemente (n parametru dat), evaluați-le și afișați calitatea maximă.

import numpy as np

def obj_f(x, a):
    return np.dot(a, x)

def gen(dim):
    pop = []
    
    for i in range(dim):
        x = np.random.choice([-1, 1], size=10)
        pop.append(x)
    
    return pop

def eval_pop(pop, a):
    quality_values = [obj_f(x, a) for x in pop]
    return quality_values

def find_max_quality(quality_values):
    max_quality = max(quality_values)
    return max_quality

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

pop = gen(30)

quality_values = eval_pop(pop, a)

max_quality = find_max_quality(quality_values)

print(f"Maximum quality found: {max_quality}")