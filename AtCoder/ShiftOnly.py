n = int(input())
arr = list(map(int, input().split()))

l = len(arr)

def shift(l, arr):
    count = 0
    for i in range(l):
        if arr[i] % 2 == 0:
            arr[i] //= 2
        else:
            return count
    c

    