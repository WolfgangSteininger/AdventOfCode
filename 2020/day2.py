class Requirement:
    rangeMin = 0
    rangeMax = 0
    targetChar = ""
    password = ""


def getinput(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            params = line.split()
            requ = Requirement()
            requ.rangeMin = int(params[0].split('-')[0])
            requ.rangeMax = int(params[0].split('-')[1])
            # remove : char
            requ.targetChar = params[1].replace(':', '')
            requ.password = params[2]
            values.append(requ)

    return values


def puzzle1():
    values = getinput('input_day2')
    correctcount = 0
    for pwd in values:
        targetcount = pwd.password.count(pwd.targetChar)
        if pwd.rangeMin <= targetcount <= pwd.rangeMax:
            correctcount += 1

    return correctcount


def puzzle2():
    values = getinput('input_day2')
    correctcount = 0
    for pwd in values:
        if (pwd.password[pwd.rangeMin-1] == pwd.targetChar and not pwd.password[pwd.rangeMax-1] == pwd.targetChar) or (not pwd.password[pwd.rangeMin-1] == pwd.targetChar and pwd.password[pwd.rangeMax-1] == pwd.targetChar):
            correctcount += 1

    return correctcount


print(puzzle1())
print(puzzle2())
