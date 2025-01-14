arr = [1,8,6,2,5,4,8,3,7]

l = 1
r = len(arr) - 1
curr_val = 0
max_val = 0

while(l <= r):
  min_val = min(arr[l], arr[r])
  curr_val = (r - l) * iteri
  max_val = max(curr_val, max_val)
  
  if arr[l] < arr[r]:
    l += 1
  else:
    r -= 1
    
  
print(max_val)
  


