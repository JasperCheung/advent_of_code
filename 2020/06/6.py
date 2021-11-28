def part_1():
    ret = 0
    with open('input.txt', 'r') as file:
        return check_answers(file)

def check_answers(f):
    ret = 0
    ans = set()
    for line in f:
        if(line == "\n"):
            print(len(ans),ans)
            ret += len(ans)
            ans = set()
        else:
            line = line.strip()
            for c in line:
                ans.add(c)
    ret += len(ans)
    ans = set()
    return ret

def part_2():
    ret = 0
    with open('input.txt', 'r') as file:
        return check_answers2(file)


def check_answers2(f):
    ret = 0
    accum = []
    for line in f:
        if(line == "\n"):
            ret += intersect(accum)
            accum = []
        else:
            line = line.strip()
            accum.append(line)

    ret += intersect(accum)
    accum = []
    return ret

def intersect(l):
    import functools

    l = [set(s) for s in l]

    return len((functools.reduce(lambda a,b : a.intersection(b),l)))





#print(part_1())
print(part_2())
