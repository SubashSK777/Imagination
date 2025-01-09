arr = [4, 7, 8, 12, 45, 99]

target = 45
L = 0
U = (len(arr)) - 1
Mid = (U + L) // 2

if target == arr[Mid]:
  print(Mid)
else:
  if arr[Mid] > target:
    R = Mid
  elif arr[Mid] < target:
    L = Mid
  

    
