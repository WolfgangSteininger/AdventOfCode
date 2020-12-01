from inputloader import *

def puzzle1():
    values = getInput('input_day1')
    for a in values:
        for b in values:
            if a + b == targetSum:
                return a * b

def puzzle2():
    values = getInput('input_day1')
    for a in values:
        for b in values:
            if a+b > targetSum:
                continue
            for c in values:
                if a + b + c == targetSum:
                    return a * b * c


targetSum = 2020

print(puzzle1())
print(puzzle2())
