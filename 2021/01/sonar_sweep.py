arr = []
with open('input.txt', 'r') as file:
    for line in file:
        arr.append(int(line))

ret = 0
for i in range(1,len(arr)):
    if arr[i] > arr[i-1]:
        ret += 1

print(ret)


ret = 0
for i in range(4, len(arr) + 1):
    if sum(arr[i-3:i]) > sum(arr[i-4:i-1]):

        ret += 1

print(ret)
