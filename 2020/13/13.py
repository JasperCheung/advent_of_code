from functools import reduce
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def part_1():
    with open('input.txt', 'r') as file:
        time = int(file.readline().strip())
        buses = file.readline().strip().split(",")

    return earliest_depart(time,buses)

def earliest_depart(time,buses):
    time = int(time)
    buses = [int(bus) if bus.isnumeric() else bus for bus in buses]
    valid_buses = [bus for bus in buses if bus != "x"]
    closest_differences = []
    for bus in valid_buses:
        closest_differences.append(least_num_greater(bus,time))
    sorted_times = sorted(enumerate(closest_differences),key=lambda x: x[1])
    ret_id = valid_buses[sorted_times[0][0]]
    ret_time = sorted_times[0][1]
    #print(ret_id, ret_time)
    return ret_id * (ret_time - time)

def part_2():
    with open('input.txt', 'r') as file:
        time = int(file.readline().strip())
        buses = file.readline().strip().split(",")

    return line_up(buses)

# def line_up(buses):
#     buses = [int(bus) if bus.isnumeric() else bus for bus in buses]
#     first = buses[0]
#     curr = findNum(100000000000000000000,first)
#     ret = curr//first
#     while(curr):
#         curr = first * ret
#         ans = True
#         print(curr,first,ret)
#         for i in range(1,len(buses)):
#             bus_id = buses[i]
#             if(bus_id == "x"):
#                 continue
#             else:
#                 if( (curr + i)% bus_id == 0):
#                     continue
#                 else:
#                     ans = False
#                     break
#         if(ans == True):
#             return curr
#         else:
#             ret += 1

def line_up(buses):
    n = []
    a = []
    buses = [int(bus) if bus.isnumeric() else bus for bus in buses]
    for i, bus in enumerate(buses):
        if bus == "x":
            continue
        bus = int(bus)
        n.append(bus)
        a.append((-i) % bus)
    print(n, a)
    print(chinese_remainder(n, a))


def least_num_greater(factor,target):
    start = 0
    while(factor * start < target):
        start += 1
    return factor * start

def index(factor,target):
    start = 0
    while(factor * start < target):
        print(start)
        start += 1
    return start

def findNum(N, K):
    rem = (N + K) % K;

    if (rem == 0):
        return N
    else:
        return (N + K - rem)


#xprint(part_1())
print(part_2())
