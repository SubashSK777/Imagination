n = int(input())
arr = list(map(int, input().split()))

l = len(arr)
for i in range(l):
    if arr[i] % 2 == 0:
        arr[i] //= 2
        