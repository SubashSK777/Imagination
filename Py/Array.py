map = {}

arr = [2, 7, 11, 15]

target = 9

comp = target- arr[0]
map[arr[0]] = 0

i = 1
comp = target - arr[i]
map[arr[i]] = i


print (map)

print [map[comp] , i]