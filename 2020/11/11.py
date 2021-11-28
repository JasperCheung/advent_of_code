from copy import deepcopy as dc
def part_1():
    with open('input.txt', 'r') as file:
        layout = []
        for line in file:
            line = line.strip()
            layout.append([c for c in line])
    return start_seating(layout)

def start_seating(layout):
    prev = dc(layout)
    while(True):
        tmp = dc(prev)
        for r in range(len(layout)):
            for c in range(len(layout[0])):
                curr = prev[r][c]
                occ = 0
                if(curr == "."):
                    continue
                else:
                    for d_r in range(-1,2):
                        for d_c in range(-1,2):
                           # print(d_r,d_c)
                            n_r,n_c = r + d_r, c + d_c

                            if(n_r < 0 or n_c < 0 or n_r >= len(layout) or n_c >= len(layout[0]) or (n_r,n_c) == (r,c)):
                                continue
                            else:
                                n = prev[n_r][n_c]
                                if(n == "#"):
                                    # if((0,9) == (r,c)):
                                    #     print((n_r,n_c))
                                    occ += 1
                # if((0,9) == (r,c)):
                #     print(occ)
                if(curr == "L"):
                    if(occ == 0):
                        tmp[r][c] = "#"
                else:
                    if(occ >= 4):
                        tmp[r][c] = "L"
        # print("############################")
        # for r in tmp:
        #     print(r)
        if(prev == tmp):

            return count_occupied(prev)
        prev = tmp

def count_occupied(layout):
    ret = 0
    for r in range(len(layout)):
        for c in range(len(layout[0])):
            if(layout[r][c] == "#"):
                ret += 1
    return ret


def part_2():
    with open('input.txt', 'r') as file:
        layout = []
        for line in file:
            line = line.strip()
            layout.append([c for c in line])
    return start_seating2(layout)

def start_seating2(layout):
    prev = dc(layout)
    while(True):
        tmp = dc(prev)
        for r in range(len(layout)):
            for c in range(len(layout[0])):
                curr = prev[r][c]
                occ = 0
                if(curr == "."):
                    continue
                else:
                    for d_r in range(-1,2):
                        for d_c in range(-1,2):
                           # print(d_r,d_c)
                            n_r,n_c = r + d_r, c + d_c

                            if(n_r < 0 or n_c < 0 or n_r >= len(layout) or n_c >= len(layout[0]) or (n_r,n_c) == (r,c)):
                                continue
                            else:
                                n = find_first(r,c,d_r,d_c,prev)
                                # if((8,0) == (r,c)):
                                #          print(n,d_r,d_c)

                                if(n == "#"):
                                    occ += 1
                # if((8,0) == (r,c)):
                #     print(occ)
                if(curr == "L"):
                    if(occ == 0):
                        tmp[r][c] = "#"
                else:
                    if(occ >= 5):
                        tmp[r][c] = "L"
        # print("############################")
        # for r in tmp:
        #     print(r)
        if(prev == tmp):

            return count_occupied(prev)
        prev = tmp

def find_first(r,c,n_r,n_c,layout):
    r += n_r
    c += n_c
    while(0 <= r < len(layout) and 0 <= c < len(layout[0])):
        symbol = layout[r][c]
        if(symbol == "L"):
            return "L"
        elif(symbol == "#"):
            return "#"
        else:
            r += n_r
            c += n_c
    return "."






#print(part_1())
print(part_2())
