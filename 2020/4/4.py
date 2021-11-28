def part_1():
    ret = 0
    with open('input.txt', 'r') as file:
        return validate_1(file)

def validate_1(f):
    # parse the data, look for empty lines
    ret = 0
    curr = {}
    for line in f:

        if(line == "\n"):
            if(validate_fields_1(curr)):
                ret += 1
            curr = {}
        else:
            line = line.split()
            tmp = { key:field for segment in line for key,field in [segment.split(":")]}
            curr.update(tmp)

    if(validate_fields_1(curr)):
        ret += 1
    return ret

def validate_fields_1(fields):
    FIELDS =  set(["byr", "iyr",  "eyr",  "hgt",  "hcl", "ecl",  "pid",  "cid"])

    if(FIELDS == fields.keys()):
        return True
    else:
        if("cid" not in fields.keys() and len(fields) == len(FIELDS) - 1):
            fields_set  = set(fields.keys())
            return fields_set.issubset(FIELDS)
        return False

def part_2():
    ret = 0
    with open('input.txt', 'r') as file:
        return validate_2(file)

def validate_2(f):
    # parse the data, look for empty lines
    ret = 0
    curr = {}
    for line in f:

        if(line == "\n"):
            if(validate_fields_2(curr)):
                ret += 1
            curr = {}
        else:
            line = line.split()
            tmp = { key:field for segment in line for key,field in [segment.split(":")]}
            curr.update(tmp)

    if(validate_fields_2(curr)):
        ret += 1
    return ret

def validate_fields_2(fields):
    FIELDS =  set(["byr", "iyr",  "eyr",  "hgt",  "hcl", "ecl",  "pid",  "cid"])
    if(FIELDS == fields.keys()):
        return validate_fields_helper(fields)
    else:
        if("cid" not in fields.keys() and len(fields) == len(FIELDS) - 1):
            fields_set  = set(fields.keys())
            return validate_fields_helper(fields)
        return False

def validate_fields_helper(fields):
    EYE_COLORS = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
    # check byr
    byr = int(fields["byr"])
    if(not 1920 <= byr  <= 2002):
        print("byr",byr)
        return False
    iyr = int(fields["iyr"])
    if(not 2010 <= iyr  <= 2020):
        print("iyr",iyr)
        return False

    eyr = int(fields["eyr"])
    if(not 2020 <= eyr  <= 2030):
        print("eyr",eyr)
        return False
    hgt = fields["hgt"]
    unit = hgt[-2:]
    num = int(hgt[:-2])
    if(unit == "cm"):
        if(not 150 <= num  <= 193):
            print("hgt-c",hgt,unit)
            return False
    elif(unit == "in"):
        if(not 59 <= num  <= 76):
            print("hgt-i",hgt,unit)
            return False
    else:
        print("hgt",hgt,unit)
        return False

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    hcl = fields["hcl"]
    if(hcl[0] == "#"):
        if(not check_hcl(hcl[1:])):
            print("hcl",hcl)
            return False
    else:
        print("byr",fields)
        return False

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    ecl = fields["ecl"]
    if(ecl not in EYE_COLORS):
        print("ecl",ecl)
        return False
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    pid = fields["pid"]
    if(len(pid) != 9):
        print("pid",pid)
        return False

    return True


def check_hcl(hcl):
    for c in hcl:
        c = ord(c)
        if(ord('0') <= c <= ord('9') or ord('a') <= c <= ord('f')):
            continue
        else:
            return False
    return True









print(part_1())
print(part_2())
