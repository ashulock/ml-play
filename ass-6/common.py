A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}
common = A.intersection(B).intersection(C)
union = A.union(B, C)
print("Common elements:", common)
print("Elements in at least one set:", union)