tree = '#'
free = '.'
xmax = len(open('input_day3').readline().strip())
ymax = len(open('input_day3').readlines())
sright = 3
sdwon = 1


def getinput(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.insert(len(values), list(line.strip()))

    return values


def updateposition(currentpos):
    currentpos[0] += sright
    currentpos[1] += sdwon

    if currentpos[0] >= xmax:
        currentpos[0] = currentpos[0] - xmax

    return currentpos


def puzzle1():
    values = getinput('input_day3')
    treessmashed = 0
    currentpos = [0, 0]
    rowsi = 0

    for rows in values:
        cp = rows[currentpos[0]]

        if cp == tree:
            treessmashed += 1
            rows[currentpos[0]] = 'X'
        else:
            rows[currentpos[0]] = 'O'
        print(rows)
        currentpos = updateposition(currentpos)

    return treessmashed


def puzzle2():
    values = getinput('input_day2')
    correctcount = 0
    for pwd in values:
        if (pwd.password[pwd.rangeMin - 1] == pwd.targetChar) ^ (pwd.password[pwd.rangeMax - 1] == pwd.targetChar):
            correctcount += 1

    return correctcount


print(puzzle1())
#print(puzzle2())
