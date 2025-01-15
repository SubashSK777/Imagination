from itertools import combinations
from itertools import permutations

data = [1, 2, 3]
sumu = 0
c = []
for j in range(1): 
  perm = combinations(data, 3)
  for i in perm:
    c.append(i)
    
    

print(c)