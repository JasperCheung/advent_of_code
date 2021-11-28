def part_1():
    ret = 0
    with open('input.txt', 'r') as file:
        grid = []
        for line in file:
            grid.append(line.strip())
        ret = count_trees(grid)
        return ret

def count_trees(grid):
    ret = 0
    size = len(grid[0])
    right = 3
    for i in range(1,len(grid)):
        obj = grid[i][right%size]
        if(obj == "#"):
            ret += 1
        right += 3
    return ret


def part_2():
    ret = 0
    with open('input.txt', 'r') as file:
        grid = []
        for line in file:
            grid.append(line.strip())
        ret = count_trees2(grid)
        return ret

def count_trees2(grid):
    ret = 1
    slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    for s in slopes:
        ret *= helper(grid,s)
    return ret

def helper(grid,slope):
    ret = 0
    size = len(grid[0])
    right = slope[0]
    down = slope[1]
    for i in range(down,len(grid),down):
        obj = grid[i][right%size]
        #print(i,right%size,obj)
        if(obj == "#"):
            ret += 1
        right += slope[0]
    #print(slope,ret)
    return ret

print(part_1())
print(part_2())
