from itertools import permutations

# Example: Generate permutations of a list [1, 2, 3]
data = [1, 2, 3]
result = sum(sum(p) for p in permutations(data))  # Sum each permutation and then sum all of them

print(result)
