# 0-127
# F = (u-1+l)/2
# B = (u+1+l)/2
def calctree(input, value):

    if len(input) == 1:
        if input == 'F' or input == 'L':  # lower
            return value[0]
        else:
            return value[1]

    leave = input[:1]
    newinput = input[1: len(input)]
    if leave == 'F' or leave == 'L':  # lower
        lower = value[0]
        upper = round(value[1] - 1 + value[0]) / 2

        r = calctree(newinput, (lower, upper))
    else:
        lower = round(value[1] + 1 + value[0]) / 2
        upper = value[1]

        r = calctree(newinput, (lower, upper))
    return r


def calcid(row, column):
    return row * 8 + column


def getinput(filename):
    with open(filename, 'r') as f:
        return f.readlines()


def calcrow(input):
    return calctree(input[:len(input) - 3], (0, 127))


def calccolumn(input):
    return calctree(input[len(input) - 3:], (0, 7))


def approach1():
    ids = []
    for ticket in getinput('input_day5'):
        ticket = ticket.strip()
        row = calcrow(ticket)
        column = calccolumn(ticket)
        ticketid = calcid(row, column)

        ids.append(ticketid)

    ids.sort()
    last = ids[0] - 1
    for id in ids:
        if id - last > 1:
            print(f'my ticket {id - 1}')
        last = id

    print(f'highest id: {max(ids)}')
    return ids


def alternativgauß(ids):
    upper = max(ids)
    lower = min(ids)
    ticketsum = sum(ids)
    # summenformel n*(n+1)/2  ==>   (n-(x-1))*(n+x)/2
    targetsum = ((upper - (lower - 1)) * (upper + lower)) / 2
    print(f'Gauß says {targetsum - ticketsum}')


ids = approach1()
alternativgauß(ids)


def test():
    # test
    print('==== TEST ====')
    print(calcrow('FBFBBFFRLR') == 44)
    print(calcrow('BFFFBBFRRR') == 70)
    print(calcrow('FFFBBBFRRR') == 14)
    print(calcrow('BBFFBBFRLL') == 102)
    print('==============')
    print(calccolumn('FBFBBFFRLR') == 5)
    print(calccolumn('BFFFBBFRRR') == 7)
    print(calccolumn('FFFBBBFRRR') == 7)
    print(calccolumn('BBFFBBFRLL') == 4)
    print('==============')
    print(calcid(calcrow('FBFBBFFRLR'), calccolumn('FBFBBFFRLR')) == 357)
    print(calcid(calcrow('BFFFBBFRRR'), calccolumn('BFFFBBFRRR')) == 567)
    print(calcid(calcrow('FFFBBBFRRR'), calccolumn('FFFBBBFRRR')) == 119)
    print(calcid(calcrow('BBFFBBFRLL'), calccolumn('BBFFBBFRLL')) == 820)
