def part1():

    ret = float('-inf')
    with open('input.txt', 'r') as file:
        for seat in file:
            ret = max(get_seat_id(seat), ret)
    return ret


def get_seat_id(seat):
    seat = seat.strip()
    rows = seat[:7]
    cols = seat[7:]
    low_row = 0
    high_row = 127
    # get seat row

    row_seat = get_row(rows)

    col_seat = get_col(cols)
    seat_id = (8 * row_seat) + col_seat

    return seat_id

def get_row(rows):

    low_row = 0
    high_row = 127
    # get seat row
    for symbol in rows:
        mid = (high_row + low_row) // 2
        if(symbol == "F"):
            high_row = mid
        else:
            low_row = mid + 1
    return low_row

def get_col(cols):

    low_col = 0
    high_col = 7
    for symbol in cols:
        mid = (high_col + low_col) // 2
        if(symbol == "L"):
            high_col = mid
        else:
            low_col = mid + 1

    return low_col


def part2():

    big = float('-inf')
    small = float('inf')
    arr = []

    with open('input.txt', 'r') as file:
        for seat in file:
            big = max(get_seat_id(seat), big)
            small =  min(get_seat_id(seat), small)
            arr.append(get_seat_id(seat))
    arr.sort()
    return find_my_seat(arr)

def find_my_seat(arr):
    prev = arr[0]
    for s_id in arr:
        if(s_id - prev > 1):
            return prev + 1
        prev = s_id







#print(get_seat_id("BBBFBFFLRL"))
#print(get_row("BBBFBFF"))
#print(get_col("LRL"))
print(part2())
#get_col("LLR")
