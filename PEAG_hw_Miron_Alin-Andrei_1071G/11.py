# Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓: {(𝑥, 𝑦, 𝑧, 𝑡) 𝑥, 𝑦, 𝑧, 𝑡 ∈ [−2,2], 𝑡 = 𝑥 + 𝑦 − 𝑧 } → ℝ
# 𝑓(𝑥, 𝑦, 𝑧) = 𝑡 ∙ 𝑥2 − 2𝑦 ∙ 𝑧
# Generați n elemente din spațiul soluțiilor (n parametru dat), evaluați-le și afișați calitatea maximă.

import numpy as np

def obj_f(x, y, z):
    t = x + y -z
    return t * x**2 - 2 * y * z

def gen(dim):
    sols = []
    for i in range(dim):
        x = np.random.uniform(-2, 2)
        y = np.random.uniform(-2, 2)
        z = np.random.uniform(-2, 2)
        sols.append((x, y, z))
        
    return sols

def eval_sols(sols):
    q_values = [obj_f(x, y, z) for x, y, z in sols]
    return q_values

def find_max_quality(q_values):
    max_q = max(q_values)
    return max_q

sols = gen(30)
q_values = eval_sols(sols)
max_q = find_max_quality(q_values)

print(f"\nMaximum quality found: {max_q}")