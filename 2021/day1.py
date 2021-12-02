class puzzle1():

    def getinput(self, inputstring):
        values = map(int,str.splitlines(inputstring))
        return list(values)

    def calculatedepth(self, measurements):
        start = "None"
        last = None
        largerCounter = 0
        
        for me in measurements:
           
            
            if (last is None):
                last = me
                #print (f"{me} {largerCounter}")
                continue
            
            if (last < me):
                largerCounter += 1
            
            #print (f"{me} {largerCounter}")
            last = me
        
        return largerCounter

    def getResult(self, inputString):
        return self.calculatedepth(self.getinput(inputString))

class window:
    C = None
    B = None
    A = None
    
    def sum(self):
        if (self.A is None or self.B is None or self.C is None):
            return -1
        return self.A + self.B + self.C
    
class puzzle2():

    def getinput(self, inputstring):
        values = map(int,str.splitlines(inputstring))
        return list(values)

    def calculatedepth(self, measurements):
        start = "None"
        last = None
        largerCounter = 0
        win = window()
        
        for me in measurements:
            win.C = win.B
            win.B = win.A
            win.A = me
            
            if (win.A is None or win.B is None or win.C is None):
                #print (f"{win.sum()} {largerCounter}")
                continue
            
            if (last is not None):
                if (last < win.sum()):
                    largerCounter += 1
            
            #print (f"{win.sum()} {largerCounter}")
            last = win.sum()
        
        return largerCounter

    def getResult(self, inputString):
        return self.calculatedepth(self.getinput(inputString))

 
class test:
    testinput = """199
    200
    208
    210
    200
    207
    240
    269
    260
    263"""

    testresult1 = 7
    testresult2 = 5
    
    tester = puzzle1()
    print(f"result t1={testresult1 == tester.getResult(testinput)}")
    tester = puzzle2()
    print(f"result t2={testresult2 == tester.getResult(testinput)}")
    
    
    


test()

f = open('2021/inputs/day_01.txt',"r")
values = f.read()

print(f"puzzle 1 = {puzzle1().getResult(values)}", end = " ")
print(f"puzzle 2 = {puzzle2().getResult(values)}")