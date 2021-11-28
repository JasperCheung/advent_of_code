import collections
def part_1():
    ret = 0
    with open('short.txt', 'r') as file:
        ret = []
        for line in file:
            line = line.strip()
            line = line.split(",")
            adder = process_line(line)
            ret.append(adder)
    return process_ret(ret) - 1

def process_line(line):
    """
    return [bag, can_hold, can_hold]
    return [bag] # if can't hold anything
    """
    first_part = line[0].split("contain")
    first_bag = first_part[0][:f(first_part[0]) - 1]
    line[0] = first_part[1]

    ret = [first_bag]
    if("no other bags" in line[0]):
        return ret
    for info in line:
        info = info.split()
        num,one,two,_ = info
        ret.append(one + " " + two)
    return ret


def process_ret(info):
    tree = {}
    for bags in info:
        #print(bags)
        if(len(bags) == 1):
            continue
        else:
            first_bag = bags[0]
            #print(first_bag)
            for color in bags[1:]:
                if(color not in tree):
                    tree[color] = []
                tree[color].append(first_bag)
    print(tree)

    return bfs(tree)

def bfs(t):
    #print(t)
    seen = set()
    q = collections.deque(["shiny gold"])
    while(q):
        curr = q.popleft()
        #print(curr)
        seen.add(curr)
        if(curr not in t):
            continue
        else:
            for children in t[curr]:
                q.append(children)
    #print(seen)
    return len(seen)


def f(s):
    return s.find("bag")


### part 2
def part_2():
    ret = 0
    with open('input.txt', 'r') as file:
        ret = []
        for line in file:
            line = line.strip()
            line = line.split(",")
            adder = process_line_2(line)
            ret.append(adder)
    return process_ret_2(ret) - 1

def process_line_2(line):
    """
    return [bag, can_hold num, can_hold num]
    return [bag] # if can't hold anything
    """
    first_part = line[0].split("contain")
    first_bag = first_part[0][:f(first_part[0]) - 1]
    line[0] = first_part[1]

    ret = [first_bag]
    if("no other bags" in line[0]):
        return ret
    for info in line:
        info = info.split()
        num,one,two,_ = info
        ret.append((one + " " + two, int(num)))
    return ret




def process_ret_2(info):
    #print(info)
    tree = {}
    for bags in info:
        first_bag = bags[0]
        if(len(bags) == 1):
            tree[first_bag] = None
        else:
            if(first_bag not in tree):
                tree[first_bag] = []
            for color in bags[1:]:
                tree[first_bag].append(color)
    return dfs(1,"shiny gold",tree)

def dfs(num,color,t):
    if(t[color] == None):
        return num
    else:
        total_sum = 0
        for children in t[color]:
            c_color, c_num = children
            total_sum += dfs(c_num,c_color,t)
        return (total_sum * num) + num





#print(part_1())
print(part_2())
