# str1 = "ABABABAB"
# str2 = "ABA"
# def returning(str1 , str2):
#   if len(str1) > len(str2):
#     base = str2
#     maxi = str1
#     mini = str2
#   else:
#     base = str1
#     maxi = str2
#     mini = str1
    
#   nmax = len(maxi)
#   nmini = len(mini)
#   count = 0
#   while (len(base) > 0):
#     if count == 1 :
#       break
#     if len(base) == 1:
#       count += 1
#     if (nmax % len(base) == 0 and nmini % len(base) == 0):
#       remax = nmax // len(base)
#       remini = nmini // len(base)   
#       if (base * remax == maxi and base * remini == mini):
#         return (base)
#       else:    
#         base = base.removesuffix(base[-1])
#     else:    
#       base = base.removesuffix(base[-1])
#   return ""


# print(returning("abaaba","ab"))

arr = [1, 3, 5, 0, 0, 4]

for i in arr:
  if i == 0:
    chang = arr.pop(i)
    arr.append(chang)
    	        
print(arr)
