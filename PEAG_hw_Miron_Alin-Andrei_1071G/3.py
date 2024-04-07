# Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓: {𝑥 = (𝑥1, … , 𝑥10) 𝑥𝑖 ∈ [−1,1], 𝑥1 + ⋯ + 𝑥9 = 1 − 𝑥10} → ℝ
# 𝑓(𝑥) = 𝑎1 ∙ 𝑥1 + ⋯ + 𝑎10 ∙ 𝑥10
# unde 𝑎 = (𝑎1, … , 𝑎10) este un vector constant, dată de intrare.
# Generați 10 elemente din spațiul soluțiilor, evaluați-le și afișați valorea medie obținută

import numpy as np

def obj_f(x, a):
    return np.dot(a, x)

def gen(dim):
    sol = []
    
    for i in range(dim):
        x = np.random.uniform(-1, 1, size = dim)
        x[9] = 1 - np.sum(x[:9])
        sol.append(x)
    
    return sol

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

sol = gen(10)
values = [obj_f(x, a) for x in sol]
avg_val = np.mean(values)

print("Solutions:\n")
for i, x in enumerate(sol):
    print(f"Solution {i + 1}: {x} - Value of f: {values[i]}")
    
print(f"\nAverage value of f: {avg_val}")