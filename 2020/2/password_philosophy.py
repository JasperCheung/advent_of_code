def part_1():
    ret = 0
    with open('input.txt', 'r') as file:
        for line in file:
            if(validate_pass(line)):
                ret += 1
    return ret

def validate_pass(line):
    line = line.split()
    limits = line[0].split("-")
    letter = line[1][0]
    string = line[2]
    least,most = int(limits[0]),int(limits[1])
    count = string.count(letter)
    return least <= count <= most


print(part_1())


def part_2():
    ret = 0
    with open('input.txt', 'r') as file:
        for line in file:
            if(validate_pass2(line)):
                ret += 1
    return ret


def validate_pass2(line):
    line = line.split()
    limits = line[0].split("-")
    letter = line[1][0]
    string = line[2]
    i1,i2 = int(limits[0]) - 1,int(limits[1]) - 1
    i1 = string[i1] == letter
    i2 = string[i2] == letter
    return i1 ^ i2

print(part_2())
