def part_1():
    with open('input.txt', 'r') as file:
        arr = []
        for line in file:
            line = line.strip()
            arr.append(int(line))
    return process_jolts(arr)

def process_jolts(arr):
    arr.sort()
    curr = 0
    one = 0
    three = 0
    for jolt in arr:
        if(jolt - curr == 3):
            three += 1
        elif(jolt - curr == 1):
            one += 1
        curr = jolt
    three += 1
    return three * one

def part_2():
    with open('input.txt', 'r') as file:
        arr = []
        for line in file:
            line = line.strip()
            arr.append(int(line))
    return find_permutations(arr)

def find_permutations(arr):
    arr.sort()
    return permute(0,arr)

# # too slow
# def permute(curr,arr):
#     print(curr,arr)
#     if(not arr):
#         return 1
#     else:

#         total = 0
#         for i in range(3):
#             if(i >= len(arr)):
#                 break
#             next = arr[i]
#             if(next - curr <= 3):
#                 total += permute(next,arr[i+1:])
#             else:
#                 break
#         return total

# [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
# [1, 2, 3, 5]

def permute(curr,arr):
    dp = [0] * (len(arr) + 1)
    dp[0] = 1
    arr = [0] + arr
    for i in range(1,len(arr)):
        curr = arr[i]
        for d in range(1,4):
            tmp_index = i - d
            if(tmp_index < 0):
                break
            prev = arr[tmp_index]
            #print(prev)
            if(curr - prev <= 3):
                dp[i] += dp[tmp_index]
            else:
                break
    print(dp)
    return dp[-1]




print(part_1())
print(part_2())
