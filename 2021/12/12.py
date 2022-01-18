def part_1(file_name):
    graph = {}
    ret = 0
    NOT_CAVES = ["start", "end"]
    with open(file_name) as f:
        for line in f:
            one, two = line.strip().split("-")
            if one not in NOT_CAVES and two not in NOT_CAVES:
                add_to_graph(graph, two, one)
            elif(two == "start" or one == "end"):
                one, two = two, one
            add_to_graph(graph, one, two)
    print(graph)
    ans = []
    num_paths = dfs(graph, "start", set(), [], ans)
    return num_paths



def add_to_graph(graph, k, v):
    if k not in graph:
        graph[k] = []
    graph[k].append(v)

def dfs(graph, cave, seen, path, ans):
    path = path + [cave]
    #print(path)
    if cave == "end":
        ans.append(path)
        return 1
    else:
        ret = 0
        if(cave.islower()):
            seen.add(cave)
        for con in graph[cave]:
            if con not in seen:
                ret += dfs(graph, con, seen, path, ans)
        if(cave in seen):
            seen.remove(cave)
        return ret


def dfs2(graph, cave, seen, path, ans, twice):
    path = path + [cave]
    print(path)
    if cave == "end":
        ans.append(path)
        return 1
    else:
        ret = 0
        if(cave.islower()):
            seen.add(cave)
        for con in graph[cave]:
            print("ASSAD", cave + " : " + con)
            if con not in seen:
                ret += dfs2(graph, con, seen, path, ans, twice)
            else:
                seen2 = set(seen)
                ret += dfs(graph, con, seen2, path[:], ans )
        if(cave in seen):
            seen.remove(cave)

        return ret

def part_2(file_name):
    graph = {}
    ret = 0
    NOT_CAVES = ["start", "end"]
    with open(file_name) as f:
        for line in f:
            one, two = line.strip().split("-")
            if one not in NOT_CAVES and two not in NOT_CAVES:
                add_to_graph(graph, two, one)
            elif(two == "start" or one == "end"):
                one, two = two, one
            add_to_graph(graph, one, two)
    print(graph)
    ans = []
    num_paths = dfs2(graph, "start", set(), [], ans, False)

    print(num_paths)
    return ret



#print(part_1("example.txt"))
print(part_2("input.txt"))
