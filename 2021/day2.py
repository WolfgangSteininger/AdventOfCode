import functools

class puzzle1():

    def getinput(self, inputstring):
        values = str.splitlines(inputstring)
        values = list(map(lambda x: str.split(x, " "), values ))
        return list(values)

    def calculatedepth(self, measurements):
        
        #result = functools.reduce(lambda a,b: a+int(b[1]) if b[0] == "down" else a, measurements) 
        #up
        #forward
        h = 0
        p = 0
        
        for m in measurements:
            v = int(m[1])
            if m[0] == "down":
                h = h + v
            elif m[0] == "up":
                h = h - v
            elif m[0] == "forward":
                p += v
        
        return p*h

    def getResult(self, inputString):
        return self.calculatedepth(self.getinput(inputString))


    
class puzzle2():

    def getinput(self, inputstring):
        values = str.splitlines(inputstring)
        values = list(map(lambda x: str.split(x, " "), values ))
        return list(values)

    def calculatedepth(self, measurements):
        aim = 0
        h = 0
        p = 0
        
        for m in measurements:
            v = int(m[1])
            if m[0] == "down":
                aim = aim + v
            elif m[0] == "up":
                aim = aim - v
            elif m[0] == "forward":
                p += v
                h = h + aim*v
        
        return p*h

    def getResult(self, inputString):
        return self.calculatedepth(self.getinput(inputString))

 
class test:
    testinput = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    testresult1 = 150
    testresult2 = 900
    
    tester = puzzle1()
    print(f"result t1={testresult1 == tester.getResult(testinput)}")
    tester = puzzle2()
    print(f"result t2={testresult2 == tester.getResult(testinput)}")

test()

f = open('2021/inputs/day_02.txt',"r")
values = f.read()

print(f"puzzle 1 = {puzzle1().getResult(values)}", end = " ")
print(f"puzzle 2 = {puzzle2().getResult(values)}")