

with open('input.txt', 'r') as file:
    cords_covered = {}
    for line in file:
        parsed_line = line.strip().split("->")
        c1,c2 = parsed_line
        x1,y1 = [int(n) for n in c1.strip().split(",")]
        x2,y2 = [int(n) for n in c2.strip().split(",")]

        if (x1 == x2):
            for y in range(min(y1,y2), max(y1,y2) + 1):
                key = (x1, y)
                if key not in cords_covered:
                    cords_covered[key] = 0
                cords_covered[key] += 1
        elif(y1 == y2):
            for x in range(min(x1,x2), max(x1,x2) + 1):
                key = (x, y1)
                if key not in cords_covered:
                    cords_covered[key] = 0
                cords_covered[key] += 1

        # part 2
        elif(abs(x1 - x2) == abs(y1 - y2)):
            if x1 > x2:
                x1, y1, x2, y2 = x2, y2, x1, y1
            slope = 1
            if(y2 < y1):
                slope = -1
            x, y = x1,y1
            while(True):
                key = (x, y)
                if key not in cords_covered:
                    cords_covered[key] = 0
                cords_covered[key] += 1
                if(y == y2):
                    break
                x += 1
                y += slope


    ret = 0
    for v in cords_covered.values():
        if(v >= 2):
            ret += 1
    print(ret)
