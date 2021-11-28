def part_1():
    with open('input.txt', 'r') as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return sum_mem(instructions)

# def sum_mem(instructions):
#     mask = 0
#     writing_mem = []
#     mask = instructions[0].split("=")[1].strip()
#     ones = "".join([c if c == "1" else "0" for c in mask])
#     zeros = "".join([c if c == "0" else "1" for c in mask])
#     ones = int(ones,base=2)
#     zeros = int(zeros,base=2)
#     instructions = instructions[1:]
#     modified = []
#     for ins in instructions:
#         ins = ins.replace(" ", "")

#         first, second = ins.split("=")
#         print(first)
#         location = int(first[4:-1])
#         num = int(second)
#         modified.append((location,num))
#     memory = {}
#     for location,num in modified:
#         changed = num
#         changed = changed  &  zeros
#         changed = changed | ones
#         memory[location] = changed

#     return sum(memory.values())


def sum_mem(instructions):
    ret = 0
    masks = []
    groups = []
    tmp = []
    for ins in instructions:
        if(ins.find("mask") != -1):
            masks.append(ins)
            if(tmp):
                groups.append(tmp)
                tmp = []
        else:
            tmp.append(ins)
    groups.append(tmp)
    memory = {}
    for i in range(len(masks)):
        curr_mask = masks[i]
        curr_group = groups[i]
        mask = curr_mask.split("=")[1].strip()
        ones = "".join([c if c == "1" else "0" for c in mask])
        zeros = "".join([c if c == "0" else "1" for c in mask])
        ones = int(ones,base=2)
        zeros = int(zeros,base=2)
        modified = []
        for ins in curr_group:
            ins = ins.replace(" ", "")
            first, second = ins.split("=")
            location = int(first[4:-1])
            num = int(second)
            modified.append((location,num))
        for location,num in modified:
            changed = num
            changed = changed  &  zeros
            changed = changed | ones
            memory[location] = changed

    return sum(memory.values())


def part_2():
    with open('input.txt', 'r') as file:
        instructions = []
        for line in file:
            instructions.append(line.strip())
    return sum_mem2(instructions)

def sum_mem2(instructions):
    ret = 0
    masks = []
    groups = []
    tmp = []
    for ins in instructions:
        if(ins.find("mask") != -1):
            masks.append(ins)
            if(tmp):
                groups.append(tmp)
                tmp = []
        else:
            tmp.append(ins)
    groups.append(tmp)
    memory = {}
    for i in range(len(masks)):
        curr_mask = masks[i]
        curr_group = groups[i]
        mask = curr_mask.split("=")[1].strip()
        ones = "".join([c if c == "1" else "0" for c in mask])
        ones = int(ones,base=2)
        modified = []

        x_index = []
        # find indexes of "X"
        for i in range(len(mask)):
            if(mask[i] == "X"):
                x_index.append(i)


        for ins in curr_group:
            ins = ins.replace(" ", "")
            first, second = ins.split("=")
            location = int(first[4:-1])
            num = int(second)
            modified.append((location,num))

        for location,num in modified:
            changed = location
            changed = changed | ones
            changed = "{0:b}".format(changed)
            changed = prepend(changed)
            for i in x_index:
                changed= changed[:i] + "X" + changed[i+1:]
            addresses = generate_addresses(changed,x_index)
            print(addresses)
            addresses = [int(x,base=2) for x in addresses]
            num = int(num)
            for addy in addresses:
                memory[addy] = num
    return sum(memory.values())

def generate_addresses(target, x_index):
    ret = []
    helper(target,x_index,ret)
    return ret

def helper(target,x_index,ret):
    if(not x_index):
        ret.append(target)
        return
    else:
        index = x_index[0]
        one = target[:index] + "1" + target[index+1:]
        zero = target[:index] + "0" + target[index+1:]
        helper(one,x_index[1:],ret)
        helper(zero,x_index[1:],ret)
        return




def prepend(s):
    return ("0" * (36 - len(s))) + s







#print(part_1())
print(part_2())
