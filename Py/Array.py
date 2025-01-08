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

while (len(base) > 0):
  if (nmax % len(base) == 0 and nmini % len(base) == 0):
    remax = 