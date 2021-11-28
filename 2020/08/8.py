def part_1():
    with open('input.txt', 'r') as file:
        cmds = []
        for line in file:
            line = line.strip()
            cmds.append(line)
    return run_game(cmds)


def run_game(cmds):
    commands_ran = set()
    index = 0
    score = 0
    while(index != len(cmds)):
        if(index in commands_ran):
            # print(index)
            return score
        else:

            commands_ran.add(index)
            curr = cmds[index]
            #print("index:", index, curr)
            command, sign_num = curr.split(" ")
            sign, num = sign_num[0] + "1", sign_num[1:]
            num = int(num)
            sign = int(sign)
            if(command == "nop"):
                index += 1
            elif(command == "acc"):
                score += sign * num
                index += 1
            else:
                # print(index, sign * num, curr)
                index += sign * num

        #print("score:", score)

    return score


def part_2():
    with open('input.txt', 'r') as file:
        cmds = []
        for line in file:
            line = line.strip()
            cmds.append(line)
    return fix_game(cmds)


def fix_game(cmds):
    for i in range(len(cmds)):
        copy = cmds[:]
        curr= copy[i]
        command, sign_num= curr.split(" ")
        if(command == "jmp"):
            edit = "nop"
        elif(command == "nop"):
            edit = "jmp"
        else:
            continue
        print("command",curr)
        copy[i] = edit + " " + sign_num
        if( not loop_or_nah(copy)):
            print("modify command num: ", i)
            return run_game(copy)


def loop_or_nah(cmds):
    commands_ran = set()
    index = 0
    while(index != len(cmds)):
        if(index in commands_ran):
            return True
        else:

            commands_ran.add(index)
            curr = cmds[index]
            command, sign_num = curr.split(" ")
            sign, num = sign_num[0] + "1", sign_num[1:]
            num = int(num)
            sign = int(sign)
            if(command == "nop"):
                index += 1
            elif(command == "acc"):
                index += 1
            else:
                index += sign * num
    return False


print(part_1())
print(part_2())
