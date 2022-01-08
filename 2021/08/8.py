def part_1(file_name):
    signals = []
    with open(file_name) as f:
        for line in f:
            patterns, out_val = line.split("|")
            patterns = patterns.strip().split(" ")
            out_val = out_val.strip().split(" ")
            signals.append((patterns, out_val))
    return find_unique_occurances(signals)

def find_unique_occurances(data):
    ret = 0
    valid = {2,3,4,7}
    for line in data:
        _, out_val = line
        for output in out_val:
            if len(output)in valid:
                ret += 1
    return ret


def part_2(file_name):
    signals = []
    with open(file_name) as f:
        for line in f:
            patterns, out_val = line.split("|")
            patterns = patterns.strip().split(" ")
            out_val = out_val.strip().split(" ")
            signals.append((patterns, out_val))
    ret = 0
    for p, o in signals:
        c = unscramble(p)
        ret += build_number(c,o)
    return ret


def unscramble(pattern):
    cipher = {}
    for i in range(10):
        cipher[i] = ""

    pattern = [set(p) for p in pattern]
    # find easy numbers
    for pat in pattern:
        p_size  = len(pat)
        if(p_size == 2):
            cipher[1] = pat
        if(p_size == 4):
            cipher[4] = pat
        if(p_size == 3):
            cipher[7] = pat
        if(p_size == 7):
            cipher[8] = pat
    bd = cipher[4] - cipher[1]
    # find 5, 6, 9
    for pat in pattern:
        if(len(pat) == 5):
            if bd.issubset(pat):
                cipher[5] = pat
            elif cipher[1].issubset(pat):
                cipher[3] = pat
            else:
                cipher[2] = pat
        elif(len(pat) == 6):
            if( cipher[7].issubset(pat)):
                if(bd.issubset(pat)):
                    cipher[9] = pat
                else:
                    cipher[0] = pat
            else:
                cipher[6] = pat
    inv_map = {"".join(sorted("".join(v))): k for k, v in cipher.items()}
    return inv_map

def build_number(cipher, outs):
    ret = ""
    for o in outs:
        ret += str(cipher["".join(sorted(o))])
    return int(ret)

print(part_1("input.txt"))
print(part_2("input.txt"))
# example_line = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"
# example_line = "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe"
# ep, eo = example_line.split("|")
# ep = ep.split()
# eo = eo.split()
# c = unscramble(ep)
# print(c)
# print(build_number(c, eo))
