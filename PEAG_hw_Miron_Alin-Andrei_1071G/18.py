# Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓: {𝑥 = (𝑥1, … , 𝑥8) 𝑥𝑖 ∈ {−1,1}, 𝑥1 + 𝑥2 + 𝑥3 + 𝑥4 ≥ 𝑥5 + 𝑥6 + 𝑥7 + 𝑥8} → ℝ
# 𝑓(𝑥) = 𝑥1 + 𝑥2 + 𝑥3 + 𝑥4 − (𝑥5 + 𝑥6 + 𝑥7 + 𝑥8)
# Generați n elemente din spațiul soluțiilor (n parametru dat), evaluați-le și afișați calitatea maximă.

import numpy as np

def obj_f(x):
    return x[0] + x[1] + x[2] + x[3] - (x[4] + x[5] + x[6] + x[7])

def gen(dim):
    sols = []
    
    for i in range(dim):
        x = np.random.choice([-1, 1], size=8)
        sols.append(x)
    
    return sols

def eval_sols(sols):
    quality_values = [obj_f(x) for x in sols]
    return quality_values

def find_max_quality(q_values):
    max_q = max(q_values)
    return max_q

sols = gen(30)
q_values = eval_sols(sols)

max_quality = find_max_quality(q_values)
print(f"\nMaximum quality found: {max_quality}")