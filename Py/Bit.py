n = 7

for i in range (2, n**0.5):
  if n % i == 0:
    print("Prime")
    break
  print("Not Prime")