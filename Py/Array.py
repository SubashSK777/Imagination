arr = ["a","aba","ababa","aa"]

count = 0

n = len(arr)

for i in range (n):
  for j in range (n):
    if arr[i] in arr[j]:
      count += 1
      
print(count)
  