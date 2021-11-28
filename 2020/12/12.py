def part_1():
    with open('input.txt', 'r') as file:
        ret = []
        for line in file:
            line = line.strip()
            ret.append(line)
    return find_dist(ret)

def find_dist(cords):
    # clean up cords
    cords = [(c[0],int(c[1:])) for c in cords]
    WE_NS = [0,0]
    facing = 0
    rotate = ["E","S","W","N"]
    adding = {
        "E":(0,1),
        "S": (1,-1),
        "W":(0,-1),
        "N": (1,1)
    }
    for cmd,num in cords:
        if(cmd == "F"):
            direction = rotate[facing]
            one,two = adding[direction]
            num *= two
            WE_NS[one] += num
        elif(cmd == "R"):
            num //= 90
            facing += num
            facing %= 4
        elif(cmd == "L"):
            num //= 90
            facing -= num
            facing %= 4
        else:
            one,two = adding[cmd]
            num *= two
            WE_NS[one] += num
    return abs(WE_NS[0]) + abs(WE_NS[1])

def part_2():
    with open('input.txt', 'r') as file:
        ret = []
        for line in file:
            line = line.strip()
            ret.append(line)
    return find_dist_waypoint(ret)

def find_dist_waypoint(cords):
    # clean up cords
    cords = [(c[0],int(c[1:])) for c in cords]
    WE_NS = [0,0]
    waypoint = [10,1]
    adding = {
        "E":(0,1),
        "S": (1,-1),
        "W":(0,-1),
        "N": (1,1)
    }
    # CW == R x,y = y,-x
    # CCW == L x,y = -y,x
    for cmd,num in cords:
        if(cmd == "F"):
            d_we, d_ns = num * waypoint[0], num * waypoint[1]
            WE_NS[0] += d_we
            WE_NS[1] += d_ns

        elif(cmd == "R"):
            num //= 90
            for i in range(num):
                waypoint[0],waypoint[1] = waypoint[1], - waypoint[0]
        elif(cmd == "L"):
            num //= 90
            for i in range(num):
                waypoint[0],waypoint[1] = -waypoint[1], waypoint[0]
        else:
            one,two = adding[cmd]
            num *= two
            waypoint[one] += num

    return abs(WE_NS[0]) + abs(WE_NS[1])



print(part_1())
print(part_2())
