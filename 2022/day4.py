total=0
for items in open('2022/inputs/day4.txt', 'r'):
    
    (a_start,a_end),(b_start,b_end) = [map(int, pair.split('-')) for pair in items.strip().split(',')]
    contains = False
    
    if (a_start >= b_start and a_end <= b_end):
        contains = True
    elif (b_start >= a_start and b_end <= a_end):
        contains = True

    if (contains):
        total = total +1

print(total)

### part 2
total=0
for items in open('2022/inputs/day4.txt', 'r'):
    
    (a_start,a_end),(b_start,b_end) = [map(int, pair.split('-')) for pair in items.strip().split(',')]
    contains = False
    
    if (a_start >= b_start and a_start <= b_end):
        contains = True
    elif (a_end >= b_start and a_end <= b_end):
        contains = True
    elif (b_start >= a_start and b_start <= a_end):
        contains = True
    elif (b_end >= a_start and b_end <= a_end):
        contains = True

    if (contains):
        total = total +1

print(total)