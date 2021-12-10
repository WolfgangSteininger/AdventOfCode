testdata = """2199943210
3987894921
9856789892
8767896789
9899965678"""

def prepareInput(data):
    heightmap = {}
    
    for x, line in enumerate(data.splitlines()):
        for y, height in enumerate(line):
            heightmap[(x,y)] = int(height)
    
    return heightmap

def calcMinimums(heightmap):
    sumMinimums = 0
    minimums = []
    for coords, currentHeight in heightmap.items():
        neighbours = ((coords[0]+1, coords[1]),
                      (coords[0]-1, coords[1]),
                      (coords[0], coords[1]+1),
                      (coords[0], coords[1]-1))
      
        neighboursValues = []
        for n in neighbours:
            neighboursValues.append(heightmap.get(n, 9)) # get returns default 9 if element not in list
        
        if all(n > currentHeight for n in neighboursValues):
            #print(f'risk found {currentHeight} in {neighboursValues}' )
            sumMinimums += currentHeight + 1
            minimums.append(coords)

    return sumMinimums, minimums
            
testresult1 = 15 # sum of lowest points
resultoftest1 = calcMinimums(prepareInput(testdata))
print(f"test1 = {testresult1 == resultoftest1[0]}")

f = open('2021/inputs/day_09.txt',"r")
input = f.read()
result, minimums = calcMinimums(prepareInput(input))
print(f"puzzle1:  {result}")

# puzzle 2
def getBasins(heightmap, minimums):
    allBasins = []
    for minimum in minimums:
        nextCoords = [minimum] # start
        basin = set([minimum])
            
        while nextCoords:
            x, y = nextCoords.pop()
            currentHeight = heightmap[(x,y)]
            #get neighbours
            neighbours = ((x+1, y),
                          (x-1, y),
                          (x, y+1),
                          (x, y-1))
            
            for neighbour in neighbours:
                nHeight = heightmap.get(neighbour, 9)
                if nHeight != 9 and nHeight > currentHeight: # neighbour is not a cliff and bigger than the current value
                    basin.add(neighbour)
                    nextCoords.append(neighbour)
        
        # store the size of this basin
        allBasins.append(len(basin))
    
    allBasins.sort(reverse=True)
    sizes = 1
    for basin in allBasins[:3]:
        sizes *= basin
    
    return sizes

testresult2 = 1134 # sum of lowest points
print(f"test2 = {testresult2 == getBasins(prepareInput(testdata), resultoftest1[1])}")
print(f"puzzle2:  {getBasins(prepareInput(input), minimums)}")