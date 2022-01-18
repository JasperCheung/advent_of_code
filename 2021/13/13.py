def intial_read(file_name):
    dots = []
    instructions = []


    with open(file_name) as f:
        for line in f:
            if not line or line == "\n":
                continue
            elif "fold" in line:
                instructions.append(line.strip().strip().split()[-1].split("="))
            else:
                dots.append(line.strip().split(","))


    dots = [[int(cord[0]), int(cord[1])] for cord in dots]
    instructions = [[cord[0], int(cord[1])] for cord in instructions]

    #print(dots)
    #print(instructions)
    return dots, instructions




def part_1(file_name):
    dots, instructions = intial_read(file_name)
    for instruct in instructions:
        first = set()
        # if y
        if instruct[0] == "y":
            for x, y in dots:
                if(y < instruct[1]):
                    first.add((x,y))
                elif(y > instruct[1]):
                    y = (2 * instruct[1]) - y
                    first.add((x,y))
        else:
            for x, y in dots:
                if(x < instruct[1]):
                    first.add((x,y))
                elif(x > instruct[1]):
                    x = (2 * instruct[1]) - x
                    first.add((x,y))
        dots = first


    # print(len(dots), dots)
    print_matrix(dots)





def print_matrix(dots):
    board = []
    for _ in range(40):
        board.append(["."] * 40)
    for x,y in dots:
        board[y][x] = "#"

    print('start')
    for line in board:
        print("".join(line))
    print('end')

print(part_1("input.txt"))
