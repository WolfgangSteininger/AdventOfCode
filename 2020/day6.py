from collections import Counter


def getdata(filename):
    values = []
    buffer = []
    with open(filename, 'r') as f:
        for line in f:
            if line == '\n':
                values.insert(len(values), buffer)
                buffer = []
                continue

            buffer.append(line.strip())

    values.insert(len(values), buffer)
    return values


def countpositiveanswers(answers):
    pos = 0
    for answersgroup in answers:
        pos += len(set(''.join([i for i in answersgroup])))
    return pos


def countoverlappinganswers(answers):
    all = 0
    for answersgroup in answers:
        pos = (''.join([i for i in answersgroup]))
        countedpos = Counter(pos)  # Counter counts all chars and creates a dict with char as key and sum as value
        onlyallpos = Counter(countedpos.values())[len(answersgroup)]  # count only those where the sum meets the size of the group
        all += onlyallpos

    return all


print(f'puzzle 1 = {countpositiveanswers(getdata("input_day6"))}')
print(f'puzzle 2 = {countoverlappinganswers(getdata("input_day6"))}')
