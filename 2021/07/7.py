def find_min_horizontal_1(line):
    ret = float('inf')
    for num in line:
        counter = 0
        for num2 in line:
            counter += abs(num - num2)
        ret = min(counter, ret)
    return ret

def part_1(file_name):
    line = []
    with open(file_name) as f:
        line = f.readline()

    line = line.split(',')
    line = [int(i) for i in line]
    print(find_min_horizontal_1(line))



def sum_art_seq(n):
    return ( ( 1 + n ) / 2) * n

def find_min_horizontal_2(line, limit):
    ret = float('inf')
    for num in range(limit + 1):
        counter = 0
        for num2 in line:
            counter += sum_art_seq(abs(num - num2))
        ret = min(counter, ret)
    return ret



def part_2(file_name):
    line = []
    with open(file_name) as f:
        line = f.readline()

    line = line.split(',')
    line = [int(i) for i in line]
    print(find_min_horizontal_2(line, max(line)))



part_1("example.txt")
part_2("input.txt")
