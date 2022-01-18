def part_1(file_name):
    matrix = []
    with open(file_name) as f:
        for line in f:
            matrix.append([int(num) for num in line.strip()])

    return find_lowest_points(matrix)

def is_low_point(mat, r, c):
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    val = mat[r][c]
    for dx, dy  in d:
        nx = r + dx
        ny = c + dy
        if(0 <= nx < len(mat) and 0 <= ny < len(mat[0])):
            if(mat[nx][ny] <= val ):
                return False
    return True

def find_lowest_points(mat):
    ret = 0
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if(is_low_point(mat, r, c)):
                ret += mat[r][c] + 1
    return ret

def find_basin_size(mat, r, c, prev, seen):
    d = [(0,1), (1,0), (0,-1), (-1,0)]
    if(r < 0 or c < 0 or r >= len(mat) or c >= len(mat[0])):
        return 0
    val = mat[r][c]
    if(val == 9 or val <= prev):
        return 0
    if((r,c) in seen):
        return 0
    else:
        seen.add((r,c))
        ret = 1
        for dx, dy in d:
            nx = r + dx
            ny = c + dy
            ret += find_basin_size(mat, nx, ny, val, seen)
        return ret

def add_all_basins(mat):
    ret = []
    for r in range(len(mat)):
        for c in range(len(mat[0])):
            if(is_low_point(mat, r, c)):
                ret.append(find_basin_size(mat, r, c, -1, set()))
    ret.sort()
    return ret[-1] * ret[-2] * ret[-3]







def part_2(file_name):
    matrix = []
    with open(file_name) as f:
        for line in f:
            matrix.append([int(num) for num in line.strip()])

    return add_all_basins(matrix)


print(part_1("input.txt"))
print(part_2("input.txt"))
