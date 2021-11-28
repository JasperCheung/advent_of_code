def part_1():
    with open('input.txt', 'r') as file:
        arr = []
        for line in file:
            line = line.strip()
            arr.append(int(line))
    return find_invalid(arr,25)

def find_invalid(arr,ps):
    for i in range(ps,len(arr)):
        target = arr[i]
        prev = arr[i-ps:i]
        if(not two_sum(target,prev)):
           return target
    return -1

def two_sum(target,arr):
    d = set()
    for num in arr:
        if(num in d):
            return True
        else:
            d.add(target - num)
    return False


def part_2():
    with open('input.txt', 'r') as file:
        arr = []
        for line in file:
            line = line.strip()
            arr.append(int(line))
    return break_encrypt(arr)


def break_encrypt(arr):
    target = find_invalid(arr,25)
    r = 1
    l = 0
    total_sum = sum(arr[0:2])
    while(r < len(arr)):
        if(total_sum == target):
            return max(arr[l:r+1]) + min(arr[l:r+1])
        if(total_sum < target):
            r += 1
            total_sum += arr[r]
        else:
            total_sum -= arr[l]
            l += 1


print(part_1())
print(part_2())
