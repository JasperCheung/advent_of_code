arr = []
forward = 0
depth = 0
with open('input.txt', 'r') as file:
    for line in file:
        if not line:
            continue
        command, num = line.split()
        print(command, num)
        num = int(num)
        if (command == "forward"):
            forward += num
        if command == "down":
            print(num)
            depth += num
        if command == "up":
            depth -= num
print(forward, depth)
print(forward * depth)

ret = 0
for i in range(len(arr)):
    pass

print(ret)

arr = []
forward = 0
depth = 0
aim = 0
with open('input.txt', 'r') as file:
    for line in file:

        if not line:
            continue
        command, num = line.split()
        print(command, num)
        num = int(num)
        if (command == "forward"):
            forward += num
            depth += num * aim
        if command == "down":
            aim += num
        if command == "up":
            aim -= num
        print(depth)

print(forward, depth)
print(forward * depth )
