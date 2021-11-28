def part_1():
    with open('input.txt', 'r') as file:
        ret = []
        tmp = []
        for line in file:
            if(line == "\n"):
                ret.append(tmp)
                tmp = []
            else:
                tmp.append(line.strip())
    ret.append(tmp)
    ret[1:] = [arr[1:] for arr in ret[1:]]
    return invalid_tickets(ret)

def invalid_tickets(inputs):
    fields,yours,nearby = inputs
    fields = [f.split(":")[1].strip() for f in fields]
    fields = [[s[0].strip(),s[1].strip()] for f in fields for s in [f.split("or")]]
    fields = [[(int(s[0]), int(s[1]))for ranges in arr for s in [ranges.split("-")]] for arr in fields]
    print(fields)
    nearby = [ [ int(s) for s in  ticket.split(",")] for ticket in nearby]
    invalids = []
    for ticket in nearby:

        for num in ticket:
            valid_1 = False
            for field in fields:
                valid_2 = False
                for ranges in field:
                    valid_2 = bool(check_valid(num,ranges)) or valid_2
                    print(valid_2, ranges, num)
                valid_1 = valid_2 or valid_1
            if(not valid_1):
                invalids.append(num)
    return sum(invalids)


def check_valid(num,field):
    small = field[0]
    big = field[1]
    return small <= num <= big


def part_2():
    with open('input.txt', 'r') as file:
        ret = []
        tmp = []
        for line in file:
            if(line == "\n"):
                ret.append(tmp)
                tmp = []
            else:
                tmp.append(line.strip())
    ret.append(tmp)
    ret[1:] = [arr[1:] for arr in ret[1:]]
    return find_field(ret)

def find_field(inputs):
    fields,yours,nearby = inputs
    names = [f.split(":")[0].strip() for f in fields]
    fields = [f.split(":")[1].strip() for f in fields]

    fields = [[s[0].strip(),s[1].strip()] for f in fields for s in [f.split("or")]]
    fields = [[(int(s[0]), int(s[1]))for ranges in arr for s in [ranges.split("-")]] for arr in fields]
    print(fields)
    nearby = [ [ int(s) for s in  ticket.split(",")] for ticket in nearby]
    invalids = []
    all_combos = []
    for ticket in nearby:
        possible = []
        do_not_add = False
        for num in ticket:
            can_fit = set()
            valid_1 = False
            for f_index,field in enumerate(fields):
                valid_2 = False
                for ranges in field:
                    valid_2 = bool(check_valid(num,ranges)) or valid_2


                valid_1 = valid_2 or valid_1
                if(valid_2):
                    can_fit.add(names[f_index])
            possible.append(can_fit)

            if(not valid_1):
                do_not_add = True
        if(not do_not_add):
            all_combos.append(possible)
    #print(len(all_combos))

    #for combo in all_combos:
    #    print(combo)
    print(yours)
    yours = [int(x) for s in yours for x in s.split(",")]
    departures = flatten_combo(all_combos,names)
    ret = 1
    for i in range(len(departures)):
        yes = departures[i]
        if(yes):
            ret *= yours[i]
    return ret




def flatten_combo(all_combos,names):
    ret = []
    for c in range(len(all_combos[0])):
        tmp = set(names)
        for r in range(len(all_combos)):
            # print(r,c)
            tmp = all_combos[r][c].intersection(tmp)
        ret.append(tmp)
    # remove anything that isn't departure
    modifed = []
    for combo in ret:
        new_one = set()
        for field in combo:
            if(field.find("departure") != -1):
                new_one.add(field)
        modifed.append(new_one)
    departures = narrow_pls(modifed)
    return departures

def narrow_pls(modifed):
    seen = set()
    while(True):
        go = False
        for i,field in enumerate(modifed):
            if(len(field) == 1 and max(field) not in seen):

                go = True
                single = max(field)
                seen.add(single)
                print(single)
                # remove every field that is not the single lock
                for j in range(len(modifed)):
                    if(i == j):
                        continue
                    else:
                        print(modifed)
                        if(single in modifed[j]):
                            modifed[j].remove(single)
                        print("WORD")
                        print(modifed)


        if(not go):
            break
    return [True  if field else False for field in modifed ]









#print(part_1())
print(part_2())
