n = int(input())
arr = list(map(int, input().split()))

l = len(arr)

def shift(l, arr):
    
    for i in range(l):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2
        else:
            return count
    count += 1
    shift(l, arr)

print(shift(l, arr))