def loadprogram(filename):
    values = []
    with open(filename, 'r') as f:
        for line in f:
            values.append(line.strip())

    return values


tracer = {}
callstack = []


def execute(ram, acc, index, altswitch=False):
    if index in tracer:
        print('panic stackoverflow protection')
        raise MemoryError()

    action = ram[index][:3]
    value = int(ram[index][4:])
    callstack.append((index, action, acc))
    tracer[index] = "visited"

    if altswitch:
        if action == 'nop':
            action = 'jmp'
        elif action == 'jmp':
            action = 'nop'

    if action == 'acc':
        acc += value
        index += 1
    elif action == 'nop':
        index += 1
    elif action == 'jmp':
        index += value

    return index, acc


def puzzle1():
    ram = loadprogram('input_day8')
    index = 0
    acc = 0

    try:
        while True:
            index, acc = execute(ram, acc, index)
            print(f'i = {index} acc = {acc}')
    except MemoryError:
        print(f'endless loop detected at {index}, acc was {acc}')


def puzzle2():
    print('== puzzle 2 ==')
    ram = loadprogram('input_day8')

    index = 0
    acc = 0
    exchange = 'jmp'
    switch = False
    while True:
        try:
            index, acc = execute(ram, acc, index, switch)
            switch = False

            if index == len(ram):
                print(f'=== bootloader completed: chk: {acc}')
                break
        except MemoryError:
            print(f'endless loop detected at {index}, acc was {acc} attempting repair')
            # search last 'nop' and change to jmp
            notfound = True
            lastcommand = callstack.pop()
            tracer.pop(lastcommand[0])
            while notfound:
                if len(callstack) == 0:
                    exchange = 'nop'
                    index = 0
                    acc = 0
                    break

                lastcommand = callstack.pop()
                tracer.pop(lastcommand[0])
                if lastcommand[1] == exchange:
                    switch = True
                    index = lastcommand[0]
                    acc = lastcommand[2]
                    notfound = False


puzzle1()

tracer = {}
callstack = []
print(puzzle2())
