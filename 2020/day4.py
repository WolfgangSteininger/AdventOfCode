import re

# helpful https://regexr.com/

blankline = '\n'
propertiesp1 = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
# regex craziness
propertiesp2 = {'byr': re.compile(r'\b((19)[2-9][0-9]\b)|((200)[0-3])\b'),
                'iyr': re.compile(r'\b(20)(((1)[0-9])|((2)(0)))\b'),
                'eyr': re.compile(r'\b(20)(((2)[0-9])|((3)(0)))\b'),
                'hgt': re.compile(r'\b(1([5-8][0-9])|(19[0-3]))(?=cm\b)|\b((59)|(6[0-9])|(7[0-6]))(?=in\b)'),
                'hcl': re.compile(r'^#[a-f|0-9]{6}$'),
                'ecl': re.compile(r'\b(amb|blu|brn|gry|grn|hzl|oth)\b'),
                'pid': re.compile(r'\b\d{9}\b')}


def getinput(filename):
    values = []
    buffer = ''
    with open(filename, 'r') as f:
        for line in f:
            if line == blankline:
                values.insert(len(values), buffer.strip())  # remove trailing whitespaces
                buffer = ''
                continue

            buffer += line.strip()
            buffer += ' '  # ensure that there are whitespaces between the properties

    # append last buffer too
    values.insert(len(values), buffer.strip())
    return values


def creatdict(passport):
    return dict(map(lambda x: x.split(':'), passport.split(' ')))


def puzzle1():
    passportsraw = getinput('input_day4')
    invalids = 0
    print(f'passworts in batch = {len(passportsraw)}')
    for passport in passportsraw:
        invalid = False
        for p in propertiesp1:
            if invalid:
                continue
            if passport.find(p) == -1:
                invalids += 1
                invalid = True

    print(f'invalid = {invalids}')
    print(f'valid = {len(passportsraw) - invalids}')
    return len(passportsraw) - invalids


def puzzle2():
    passportsraw = getinput('input_day4')
    invalids = 0
    print(f'passworts in batch = {len(passportsraw)}')
    for passport in passportsraw:
        invalid = False
        calcpassport = creatdict(passport)

        if len(calcpassport) < 7 or (len(calcpassport) == 7 and calcpassport.keys().__contains__('cid')):
            invalids += 1
            continue

        for p in calcpassport.items():
            if invalid:
                break
            if p[0] == 'cid':
                continue

            name = p[0]
            value = p[1]
            rule = propertiesp2[name]

            result = rule.search(value)
            if result is None:
                print(f'{name} = {value} --> {rule.search(value) is not None}')
                invalids += 1
                invalid = True

    print(f'valid = {len(passportsraw) - invalids}')
    return len(passportsraw) - invalids


# print(puzzle1())
print(puzzle2())


def test():
    for i in range(0, 20000):
        if propertiesp2['byr'].match(str(i)):
            print(i)


test()
