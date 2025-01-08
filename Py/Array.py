words = ["a","aba","ababa","aa"]

count = 0
        
length = len(words)

for i in range (length):
  n = len(words[i])
  for j in range (length):
    if i != j:
      if words[i] == words[j][:n] and words[i] == words[j][-n:]:
        count += 1
print(count)  