n = 7

for i in range (2, int(n**0.5) + 1):
  if n % i != 0:
    print("Prime")
    break
else:
  print("Not Prime")