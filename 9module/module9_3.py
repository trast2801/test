class EvenNumbers:
    def __init__(self, start=0, end=1):
        if end < start:
            end = start + 1
        self.start = start-1
        self.end = end
        #self.i = start
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            #self.i += 1
            self.start += 1
            if self.start == self.end:
                raise StopIteration()
            if (self.start % 2 == 0):
                return (self.start)

spisok = EvenNumbers(10, 25)
for i in spisok:
    print(i)