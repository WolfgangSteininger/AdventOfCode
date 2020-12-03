tree = '#'
free = '.'
xmax = len(open('input_day3').readline().strip())
ymax = len(open('input_day3').readlines())


def getinput(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.insert(len(values), list(line.strip()))

    return values


def updateposition(currentpos, sright, sdown):
    currentpos[0] += sright
    currentpos[1] += sdown

    if currentpos[0] >= xmax:
        currentpos[0] = currentpos[0] - xmax

    return currentpos


def puzzle1(speedr, speedd):
    values = getinput('input_day3')
    treessmashed = 0
    currentpos = [0, 0]

    for i in range(0,ymax, speedd):
        row = values[i]
        cp = row[currentpos[0]]

        if cp == tree:
            treessmashed += 1
            row[currentpos[0]] = 'X'
        else:
            row[currentpos[0]] = 'O'
        # print(row)
        currentpos = updateposition(currentpos, speedr, speedd)

    return treessmashed


def puzzle2():
    speeds = [1, 1], [3, 1], [5, 1], [7, 1], [1, 2]
    amountpossiblechristmastreesavailableafterallruns = 1
    for speed in speeds:
        amountpossiblechristmastreesavailableafterallruns *= (puzzle1(speed[0], speed[1]))

    return amountpossiblechristmastreesavailableafterallruns


print(puzzle1(3, 1))
print(puzzle2())
