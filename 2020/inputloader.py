def getinput(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(int(line.strip()))
    return values
