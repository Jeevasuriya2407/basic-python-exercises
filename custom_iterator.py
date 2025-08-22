class Count:
    
    def __init__(self,low,high):
        self.current=low
        self.high=high
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.high<=self.current:
            raise StopIteration
        value=self.current
        self.current+=1
        return value

for num in Count(1,5):
    print(num)
