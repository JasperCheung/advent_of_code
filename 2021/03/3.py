arr = []
with open('input.txt', 'r') as file:
    for line in file:
        if not line:
            continue
        arr.append(line.strip())


m = ""
l = ""
for i in range(len(arr[0])):
    zero = 0
    one = 0
    for n in arr:
        if(n[i] == "1"):
            one += 1
        else:
            zero += 1
    if(zero > one):
        m += ("0")
        l += ("1")
    else:
        m+=("1")
        l+=("0")

print(m, l)

print(int(m, 2) * int(l,2))
print("two")

arr2 = arr[:]
results = arr2[:]
for i in range(len(arr[0])):
    if len(results) == 1:
        break
    tmp_arr = results[:]
    results = []
    ones = []
    zeros = []
    zero = 0
    one = 0
    for n in tmp_arr:
        if(n[i] == "1"):
            one += 1
            ones.append(n)
        else:
            zero += 1
            zeros.append(n)
    if(zero > one):
        results = zeros
    else:
        results = ones

print(results)
a1 = results[0]

arr2 = arr[:]
results = arr2[:]
for i in range(len(arr[0])):
    if len(results) == 1:
        break
    tmp_arr = results[:]
    results = []
    ones = []
    zeros = []
    zero = 0
    one = 0
    for n in tmp_arr:
        if(n[i] == "1"):
            one += 1
            ones.append(n)
        else:
            zero += 1
            zeros.append(n)
    if(zero <= one):
        results = zeros
    else:
        results = ones

print(results)
a2 = results[0]

print(int(a1,2))
print(int(a2,2))
print(int(a1,2) * int(a2,2))
