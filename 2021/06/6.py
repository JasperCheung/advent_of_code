def growth_simulation(arr, n):
    for _ in range(n):
        a_c = arr[:]
        for i, fish in enumerate(arr):
            if(fish == 0):
                a_c.append(8)
                a_c[i] = 6
            else:
                a_c[i] -= 1
        arr = a_c
    return arr


def fast_simulation(arr, n):
    state = [0] * 9
    for f in arr:
        state[f] += 1
    for _  in range(n):
        c = state[:]
        for i in range(1,9):
            state[i-1] = c[i]
        state[8] = c[0]
        state[6] += c[0]

    return state



# test = growth_simulation([3,4,3,1,2], 80)
# print(test)
# print(len(test))

test2 = fast_simulation([3,4,3,1,2], 256)
print(sum(test2))
# for i in range(1,19):
#     test_3 = fast_simulation([3,4,3,1,2], i)
#     #print(i,sum(test_3), test_3)

# test4 = fast_simulation([2,3,2,0,1], 1)





# with open('example.txt', 'r') as file:
#     last_line = file.readlines()[-1]
#     days, fishes = last_line.strip().split(":")
#     fishes = [int(n) for n in fishes.split(",")]
#     day = int(days.split()[1])
#     ret = growth_simulation(fishes, 80 - day)
#     print(len(ret))



# with open('input.txt', 'r') as file:
#     line = [int(n) for n in next(file).strip().split(",")]
#     ret_1 = growth_simulation(line, 80)
#     print(len(ret_1))


with open('input.txt', 'r') as file:
    line = [int(n) for n in next(file).strip().split(",")]
    ret_2 = fast_simulation(line, 256)
    print(sum(ret_2))
