import numpy as np
print()
# the generation of a list that contains an arithmetic progression 45...-34
# with a ratio of -5
#
#generarea unei liste care contine o progresie aritmetica 45...-34 cu ratia -5

# classic for
L = []
for i in range(45, -34, -5):
    L.append(i)
    
print(f"[classic for] List L: {L}")

#list comprehension
L = [i for i in range(45, -34, -5)]
print(f"[list comprehension] List L: {L}")

print("\n------------------------------------------------------------------------------------------------\n")

# selecting the elements that are divisible by k from the list
#
#selectarea elemetelor divizibile cu k din lista

# classic for
k = 3
LP = []
for i in L:
    if i % k == 0:
        LP.append(i)
        
print(f"[classic for] Elementele divizibile cu 3 din L: {LP}")

#list comprehension
k = 3
LP = [i for i in L if i % k == 0]
print(f"[list comprehension] Elementele divizibile cu 3 din L: {LP}")

print("\n------------------------------------------------------------------------------------------------\n")

# calculating the maximum value from the list and determining its position
#
#calculul maximului din lista si determinarea pozitiei de aparitie

maximum = max(L)
index_maximum = L.index(maximum)

print(f"The maximum value from List L is: {maximum} at index: {index_maximum}")

print("\n------------------------------------------------------------------------------------------------\n")

# all position of the element in the list
#
# toate pozitiile de aparitie ale unui element intr-o lista

# classic for
t = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
all_positions = []
for index, value in enumerate(t):
    if value == 6:
        all_positions.append(index)

print("[classic for]")
print(f"Value 6 appears in the list: {t}\nIn positions: {all_positions}\n")
#list comprehension
t = [1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6]
all_positions = [index for index, value in enumerate(t) if value == 3]
print("[list comprehension]")
print(f"Value 6 appears in the list: {t}\nIn positions: {all_positions}\n")

print("\n------------------------------------------------------------------------------------------------\n")


# the generation of a set of type -1, -1+eps, -1+2*eps, ..., 1
#
# generarea unei multimi de tipul -1, -1+eps, -1+2*eps, ..., 1

# classic for
step = 0.1
L1 = []

for i in range(10000):
    if -1 + i * step <= 1:
        L1.append(-1 + i * step)
print("[classic for]")
print(f"The values from the interval [-1, 1] with the step 0.1: \n{L1}")

#list comprehension
step = 0.1
L1 = [(-1 + i * step) for i in range(10000) if (-1 + i * step) <= 1]
print("\n[list comprehension]")
print(f"The values from the interval [-1, 1] with the step 0.1: \n{L1}")

print("\n------------------------------------------------------------------------------------------------\n")
# the same using numpy
# the generation of a set of type -1, -1+eps, -1+2*eps, ..., 1
#
# generarea unei multimi de tipul -1, -1+eps, -1+2*eps, ..., 1

L2 = np.arange(-1, 1.01, 0.1)
print("[numpy arrange, equivalent of range]")
print(f"Values from the interval [-1, 1] with step 0.1: \n{L2}")