def part_1(file_name):
    ret = 0
    nav_lines = []
    with open(file_name) as f:
        for line in f:
            ret += points(find_corruption(line.strip()))


    return ret


def find_corruption(line):
    left = "([{<"
    right = ")]}>"
    pairs = {right[i]:left[i] for i in range(len(left))}
    stack  = []
    for c in line:
        if not stack:
            stack.append(c)
        else:
            if c in left:
                stack.append(c)
            else:
                if(pairs[c] == stack[-1]):
                    stack.pop()
                else:
                    return c

def points(c):
    if not c:
        return 0
    if ")" == c:
        return 3
    if "]" == c:
        return 57
    if "}" == c:
        return 1197
    if ">" == c:
        return 25137


def find_incom(line):
    left = "([{<"
    right = ")]}>"
    pairs = {right[i]:left[i] for i in range(len(left))}
    stack  = []
    for c in line:
        if not stack:
            stack.append(c)
        else:
            if c in left:
                stack.append(c)
            else:
                if(pairs[c] == stack[-1]):
                    stack.pop()
                else:
                    return ""
    return "".join(stack)


def part_2(file_name):
    ret = []
    nav_lines = []
    with open(file_name) as f:
        for line in f:
            seq = find_incom(line.strip())
            if seq:
                ret.append(points_2(seq[::-1]))

    return sorted(ret)[len(ret)//2]

def points_2(seq):
    ret = 0
    for c in seq:
        point = 0
        if "(" == c:
            point = 1
        if "[" == c:
            point = 2
        if "{" == c:
            point = 3
        if "<" == c:
            point = 4
        ret *= 5
        ret += point
    return ret




print(part_1("input.txt"))
print(part_2("input.txt"))
