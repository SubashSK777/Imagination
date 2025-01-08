str1 = "ABABABAB"
str2 = "ABA"

if len(str1) > len(str2):
  base = str2
  maxi = str1
  mini = str2
else:
  base = str1
  maxi = str2
  mini = str1
  
nmax = len(maxi)
nmini = len(mini)
print("..............")
count = 0
while (len(base) > 0):
  if count == 1 :
    break
  if len(base) == 1:
    count += 1
  print(len(base))
  if (nmax % len(base) == 0 and nmini % len(base) == 0):
    remax = nmax // len(base)
    remini = nmini // len(base)
    
    if (base * remax == maxi and base * remini == mini):
      print(base)
      break
  else:
    
    base = base.removesuffix(base[-1])
    print(base)
    

print("Errorrrrrrrrrrr")