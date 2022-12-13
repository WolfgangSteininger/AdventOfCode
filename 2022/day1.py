with open('inputs/day1.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

cals = 0
list = []

for cal in calories:
    if(cal == ""):
        list.append(cals)
        cals = 0
        continue
    cals = cals + int(cal)
    
list.append(cals)
print(f"solution 1: {max(list)}")

list.sort()
# either
#print(sum(list[-3:]))

# or
list.reverse()
print(f"solution 2: {sum(list[:3])}")