# Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓: {(𝑥, 𝑦, 𝑧) 𝑥, 𝑦, 𝑧 ∈ [−2,7], 𝑥 + 𝑦 + 𝑧 < 10} → ℝ
# 𝑓(𝑥, 𝑦, 𝑧) = 𝑥^2 − 2𝑦 ∙ 𝑧
# Generați 20 elemente din spațiul soluțiilor (candidați la soluție), evaluați-le și afișați valorile obținute.

import numpy as np

def objective_f(x, y, z):
    return x**2 - 2 * y * z

def gen(dim):
    solutions = []
    
    for i in range(dim):
        x = np.random.uniform(-2, 7)
        y = np.random.uniform(-2, 7)
        z = np.random.uniform(-2, 7)

        if x + y + z < 10:
            solutions.append((x, y, z))
        
    return solutions

solutions = gen(20)

for sol in solutions:
    x, y, z = sol
    print(f"Candidate: {sol}, Value of f: {objective_f(x, y, z)}")