def part_1(file_name):
    cal_list  = parse_input(file_name)
    cal_list = [sum(cals) for cals in cal_list]

    return max(cal_list)


def parse_input(file_name):
    cal_list = []
    with open(file_name) as f:
        single_cal_list = []
        for line in f:
            if line == "\n":
                cal_list.append(single_cal_list)
                single_cal_list = []
            else:
                single_cal_list.append(int(line))
        cal_list.append(single_cal_list)
    return cal_list

def part_2(file_name):
    cal_list  = parse_input(file_name)
    cal_list = [sum(cals) for cals in cal_list]
    return sum(sorted(cal_list)[-3:])



print(part_1("example.txt"))
print(part_1("input.txt"))
print(part_2("example.txt"))
print(part_2("input.txt"))
