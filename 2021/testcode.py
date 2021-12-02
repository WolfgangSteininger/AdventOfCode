
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
    
    
    
    
