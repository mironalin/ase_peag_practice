# Scrieți o funcție Python pentru implementarea funcției de maxim
# 𝑓: {𝑥 = (𝑥1, … , 𝑥7) 𝑥𝑖 ∈ [−10,10], 𝑥1 + ⋯ + 𝑥7 ≤ 10} → ℝ
# 𝑓(𝑥) = 𝑎1 ∙ 𝑥1 + ⋯ + 𝑎7 ∙ 𝑥7
# unde 𝑎 = (𝑎1, … , 𝑎7) este un vector constant, dată de intrare.
# Generați 10 elemente din spațiul soluțiilor, evaluați-le și afișați calitatea maximă și un individ cu acea
# calitate.

import numpy as np

def obj_f(x, a):
    return np.dot(a, x)

def gen(dim):
    sols = []
    
    for i in range(dim):
        x = np.random.randint(-10, 11, size=7)
        
        while np.sum(x) > 10:
            x = np.random.randint(-10, 11, size=7)
        
        sols.append(x)
        
    return sols

def eval_sols(sols, a):
    q_vals = [obj_f(x, a) for x in sols]
    return q_vals

def find_max_q_and_sol(sols, q_vals):
    max_q_index = np.argmax(q_vals)
    max_q = max(q_vals)
    max_q_sol = sols[max_q_index]
    
    return max_q, max_q_sol

a = np.array([1, 2, 3, 4, 5, 6, 7])

sols = gen(10)
q_vals = eval_sols(sols, a)

max_q, max_q_sol = find_max_q_and_sol(sols, q_vals)
print(f"Maximum quality found: {max_q}")
print(f"Solution with maximum quality: {max_q_sol}")
