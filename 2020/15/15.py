def part_1():
    with open('short.txt', 'r') as file:

        for line in file:
            num =(line.strip().split(","))
    return run_game(num)



def run_game(num):
    num = [int(n) for n in num]
    d = {}
    for i in range(len(num)):
        curr = num[i]
        d[curr] = [i+1]

    curr = 0
    # if(len(d[num[-1]]) == 1):
    #     turn = 0
    # else:
    #     turn = d[num[-1]][-1] - d[num[-1]][-2]

    for i in range(len(num) + 1,30000000):
        #print(i,curr)
        #print(d)
        if(curr not in d):
            d[curr] = [i]
            curr = 0
        else:

            d[curr].append(i)
            curr = d[curr][-1] - d[curr][-2]
    return curr



print(part_1())
