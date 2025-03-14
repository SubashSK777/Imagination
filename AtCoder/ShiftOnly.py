n = int(input())
arr = list(map(int, input().split()))
l = len(arr)

count = 3
def shift(l, arr,count):
    
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            
            return count
        
        else:
            arr[i] = arr[i]//2
    count += 1
    shift(l, arr,count)

print(shift(l, arr, count))