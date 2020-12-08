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
    group =0
    for answersgroup in answers:
        group += len(set(''.join([i for i in answersgroup])))
    return group



print (f'puzzle 1 = {countpositiveanswers(getdata("input_day6"))}')

