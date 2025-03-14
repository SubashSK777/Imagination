n = int(input())
arr = list(map(int, input().split()))
l = len(arr)
count = 0

flag = 1

while flag:
    for i in range(l):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2
        else:
            print(cou)
