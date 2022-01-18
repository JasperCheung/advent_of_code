import copy

def part_1(file_name):
    mat = []
    with open(file_name) as f:
        for line in f:
            mat.append([int(i) for i in line.strip()])
    ret = 0
    for _ in range(100):
        mat, flashes = next_step(mat)
        ret += flashes

    return ret


def next_step(mat):
    mat = [[n + 1 for n in line ] for line in mat]
    mat_cpy = copy.deepcopy(mat)
    while(True):
        # intial add
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                increment(mat, r, c)

        if(mat == mat_cpy):
            break
        mat_cpy = copy.deepcopy(mat)

    flashes = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if(mat[r][c] == -1):
                mat[r][c] = 0
                flashes += 1

    return mat, flashes

def increment(mat, r, c):
    v = mat[r][c]
    if(v <= 9):
        return
    else:
        mat[r][c] = -1
        for d_i in range(-1,2):
            for d_j in range(-1,2):
                if d_i == 0 and d_j == 0:
                    continue
                nr = r + d_i
                nc = c + d_j
                if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]):
                    if(mat[nr][nc] != -1):
                        mat[nr][nc] += 1


def part_2(file_name):
    mat = []
    with open(file_name) as f:
        for line in f:
            mat.append([int(i) for i in line.strip()])
    ret = 0
    while(True):
        ret += 1
        mat, flashes = next_step(mat)
        if(flashes == 100):
            break
    return ret





print(part_1("input.txt"))
print(part_2("input.txt"))
