import functools

class puzzle1():

    def getinput(self, inputstring):
        values = list(str.splitlines(inputstring))
        values = [list(lines) for lines in values]
        return list(values)

    def runDiag(self, report):
        
        linesCount = len(report)
        min = linesCount/2
        
        result = [0] * len(report[0])
        
        for line in report:
            for num in range(len(line)):
                result[num] += int(line[num]) # count all 1's in each measurement line.
            
        gamma = ''
        epsilon = ''

        # create the gamma end epsilon numbers.
        for x in result:
            if x > min:
                gamma = gamma +'1'
                epsilon = epsilon + '0'
            else:
                gamma = gamma + '0'
                epsilon = epsilon + '1'
            
        gamma = int(gamma, 2)
        epsilon = int(epsilon, 2)
        return gamma*epsilon

    def getResult(self, inputString):
        return self.runDiag(self.getinput(inputString))
    
class puzzle2():

    def getinput(self, inputstring):
        values = list(str.splitlines(inputstring))
        #values = [list(lines) for lines in values]
        return list(values)

    def runDiag(self, report):
        placeCount = len(report[0])        
        result = [0] * placeCount
        
        oxy = report.copy()
        filteroxy = ''
        place = 0
        
        while len(oxy) > 1:
            minl = len(oxy)/2
            sum1 = 0
            for line in oxy:
                sum1 += int(line[place])
            
            if (sum1 >= minl): 
                # 1 is more common at this place
                filteroxy += '1'
            else:
                # 0 is more common at this place
                filteroxy += '0'
            
            place += 1   
            oxy = list(filter(lambda binary: binary.startswith(filteroxy), oxy))
            
        co2 = report.copy()
        filterco2 = ''
        place = 0
        
        while len(co2) > 1:
            minl = len(co2)/2
            sum1 = 0
            for line in co2:
                sum1 += int(line[place])
            
            if (sum1 >= minl): 
                # 1 is more common at this place
                filterco2 += '0'
            else:
                # 0 is more common at this place
                filterco2 += '1'
            
            place += 1   
            co2 = list(filter(lambda binary: binary.startswith(filterco2), co2))
         
        oxy10 = int(oxy[0], 2)
        co210 = int(co2[0], 2)
        return oxy10*co210

    def getResult(self, inputString):
        return self.runDiag(self.getinput(inputString))
    
    
class test:
    testinput = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

    testresult1 = 198
    testresult2 = 230
    
    tester = puzzle1()
    print(f"result t1={testresult1 == tester.getResult(testinput)}")
    tester = puzzle2()
    print(f"result t2={testresult2 == tester.getResult(testinput)}")

test()

f = open('2021/inputs/day_03.txt',"r")
values = f.read()

print(f"puzzle 1 = {puzzle1().getResult(values)}", end = " ")
print(f"puzzle 2 = {puzzle2().getResult(values)}")
