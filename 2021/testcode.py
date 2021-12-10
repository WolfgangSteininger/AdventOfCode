
class Fibonacci:
    def __init__(self, max_n):
        self.MaxN = max_n
        self.N = 0
        self.A = 0
        self.B = 0
        
    def __iter__(self):
        self.N = 0
        self.A = 0
        self.B = 1
        return self
    
    def __next__(self):
        if (self.N < self.MaxN):
            self.N += 1
            self.A, self.B = self.B, self.A + self.B
            return self
        raise StopIteration


s = Fibonacci(12)

for f in s:
    #print(f, end=" ")
    print(f"A: {f.A} B: {f.B}")
    
    
    
# you are a wizard 'arrays!
testarray = [[1,2,3,4],
             [2,2,2,0],
             [0,10,3,2],
             [1,20,0,9]]


t2 = testarray.copy()
t2.remove([2,2,2,0])
print(testarray)
print(t2)
testarray[0][0] = 999
print(testarray)
print(t2)

# sum over an array/matrix
print(sum(sum(testarray, start=[])))

# using zip to transpose a matrix
print(list(zip(*testarray)))

# set returns the distinct elements of that iterable
print(set(testarray[1]))
print(set(testarray[0]))
