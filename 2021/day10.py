testdata = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

testresult1 = 26397
testresult2 = 288957

corruptRank = {')': 3,
              ']': 57,
              '}': 1197,
              '>': 25137}

missingRank = {'(': 1,
               '[': 2,
               '{': 3,
               '<': 4}

openings = ['(','[','{','<']
matches = {'(': ')',
           '[': ']',
           '{': '}',
           '<': '>',}


def getResult(data: str):
    value = 0
  
    linesMissingBrackets = []
    
    for line in data.splitlines():
        indentionStack = []
        isCorrupt = False
        for bracked in line:
            if bracked in openings:
                indentionStack.append(bracked)
                continue
            
            last = indentionStack.pop()
            if matches[last] != bracked:
                #corrupt
                value += corruptRank[bracked]
                isCorrupt = True
                break
        
        if not isCorrupt:
            linesMissingBrackets.append(line)

    return value, linesMissingBrackets

def fixErrors(data):
    linesRank = []
    
    for line in data:
        indentionStack = []
        for bracked in line:
            if bracked in openings:
                indentionStack.append(bracked)
                continue    
            last = indentionStack.pop()
        
        # stack of opening brackets... 
        rank = 0
        while indentionStack:
            #for opened in indentionStack:
            opened = indentionStack.pop()
            rank*=5
            rank+=missingRank[opened]
        
        linesRank.append(rank)
    
    linesRank.sort()
    middle = int(len(linesRank)/2)
    return linesRank[middle]

testRankValue, testMissingLines = getResult(testdata)
print(f"puzzle 1 test: {testRankValue==testresult1}")


f = open('2021/inputs/day_10.txt',"r")
input = f.read()
rankValue, missingLines = getResult(input)
print(f"puzzle 1 result: {rankValue}") #288291

# puzzle 2
print(f"puzzle 2 test: {fixErrors(testMissingLines)==testresult2}")
print(f"puzzle 2 result: {fixErrors(missingLines)}") #820045242