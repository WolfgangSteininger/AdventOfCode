total=0
for items in open('2022/inputs/day3.txt', 'r'):
    length = len(items) // 2
    f = items[:length]
    s = items[length:]

    item, = set(f) & set(s)

    prio=0
    if (ord(item) >= ord('a')):
        prio = ord(item) - ord('a') + 1
    else:
        prio = ord(item) - ord('A') + 27
    #print(f"{prio} {item}")
    total += prio

print(total)


## part 2
total = 0
with open('2022/inputs/day3.txt', 'r') as f:
    items = f.readlines()
    items = [i.strip() for i in items]
    

i = 0
while i < len(items):
    a,b,c = items[i:i+3]
    i += 3
    #print(f"{i}: {a} {b} {c}")
    badge, = set(a) & set (b) & set(c)

    prio=0
    if (ord(badge) >= ord('a')):
        prio = ord(badge) - ord('a') + 1
    else:
        prio = ord(badge) - ord('A') + 27
    #print(f"{prio} {item}")
    total += prio

    print(badge)
print(total)