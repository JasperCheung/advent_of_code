import copy
chosen = []
boards = []

with open('input.txt', 'r') as file:
    chosen = [int(n) for n in next(file).strip().split(",")]
    next(file)
    board = []
    for line in file:
        if(line == "\n"):
            boards.append(board)
            board = []
        else:
            board.append([int(n) for n in line.strip().split()])
    boards.append(board)

def simulate_game(b, chosen):
    total_sum = sum([sum(col) for col in b])
    board = copy.deepcopy(b)
    for index,num in enumerate(chosen):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == num):
                    total_sum -= num
                    board[i][j] = "x"
                    if(get_column(board, j) == ["x"] * 5 or get_row(board, i) == ["x"] * 5):
                        return total_sum, index + 1, num
    return -1, float('inf'), -1


def get_column(board, c):
    col = []
    for r in range(len(board)):
        col.append(board[r][c])
    return col

def get_row(board, r):
    return board[r][:]


def print_mat(mat):
    for r in mat:
        print(r)
    print()

ret = 0
turns = float('inf')
last_turns = float('-inf')
last_ret = 0
for index, board in enumerate(boards):

    total, turn, last = simulate_game(board, chosen)
    print(index,simulate_game(board, chosen ), total*  last)
    # print(turns)
    # print(turn)
    # print(turn < turns)
    if(turn < turns):
        turns = turn
        ret = last * total
    if(turn > last_turns):
        last_turns = turn
        last_ret = last * total


print(ret, turns)
print(last_ret, last_turns)



# #print(chosen)
# for b in boards:
# #     print_mat(b)
# print_mat(boards[22])
# print(simulate_game(boards[22], chosen))
#print_mat(boards[2])
