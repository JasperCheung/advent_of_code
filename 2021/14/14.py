STEPS = 40
def part_1(file_name):
    ret = 0
    template, rules = parse_input(file_name)
    for i in range(STEPS):
        template = step(template, rules)
        print(i + 1, ":", template)
    print(template)
    ret = diff_element(template)

    return ret


def parse_input(file_name):
    template = []

    with open(file_name) as f:
        for line in f:
            template.append(line.strip())

    rules = template[2:]
    template = template[0]
    rules = [r.split("->") for r in rules]
    rules = {r[0].strip(): r[1].strip() for r in rules}

    return template, rules


def step(template, rules):
    ret = ""
    replace = {}
    for i in range(len(template) -1):
        pair = template[i:i+2]
        if pair in rules:
            replace[i] = rules[pair]
    #print(replace)

    for i in range(len(template)):
        ret += template[i]
        if i in replace:
            ret += replace[i]

   # print("ans", ret)

    return ret

def diff_element(word):
    count = {}
    for c in word:
        if c not in count:
            count[c] = 0
        count[c] += 1
    #print("DIFF ELE:", count)
    v = count.values()
    return max(v) - min(v)

def part_2(file_name):
    ret = 0
    template, rules = parse_input(file_name)
    tmp = {}
    count = {}
    for c in template:
        if c not in count:
            count[c] = 0
        count[c] += 1
    for i in range(len(template) -1):
        pair = template[i:i+2]
        if pair not in tmp:
            tmp[pair] = 0
        tmp[pair] += 1

    template = tmp

    for i in range(STEPS):
        template, count = step_dict(template, rules, count)
        #print(i + 1, "p2 - temp", template)
        #print(i + 1, "p2 - count", count)
    ret = diff_element_dict(count)
    return ret


def step_dict(template, rules, count):
   # print(template)
    ret = {}
    for pair in template:
        r = rules[pair]
        n1, n2 = pair[0] + r,  r + pair[1]
        if(n1 not in ret):
            ret[n1] = 0
        if(n2 not in ret):
            ret[n2] = 0

        ret[n1] += template[pair]
        ret[n2] += template[pair]
        #print(pair, n1, n2, ret)
        if r not in count:
            count[r] = 0
        count[r] += template[pair]

    return ret, count

def diff_element_dict(count):
    #print(count)
    v = count.values()
    return max(v) - min(v)


#print(part_1("example.txt"))
print(part_2("input.txt"))


#debug
# print()

# s = "NNCB"
# d = {}
# for i in range(len(s)-1):
#     pair = s[i:i+2]
#     if pair not in d:
#         d[pair] = 0
#     d[pair] += 1
# print(d)

# s = "NCNBCHB"
# d = {}
# for i in range(len(s)-1):
#     pair = s[i:i+2]
#     if pair not in d:
#         d[pair] = 0
#     d[pair] += 1
# print(d)

# s = "NBCCNBBBCBHCB"
# d = {}
# for i in range(len(s)-1):
#     pair = s[i:i+2]
#     if pair not in d:
#         d[pair] = 0
#     d[pair] += 1
# print(d)
