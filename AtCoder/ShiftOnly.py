n = int(input())
arr = list(map(int, input().split()))
l = len(arr)

count = 0
def shift(l, arr,count):
    
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] != 0:
            arr[i] = arr[i]//2

    
        
        else:
            return count
    count += 1
    shift(l, arr,count)

print(shift(l, arr, count))