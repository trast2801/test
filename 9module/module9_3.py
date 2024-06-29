class EvenNumbers:
    def __init__(self, start=0, end=1):
        if end < start:
            end = start + 1
        self.start = start-1
        self.end = end
        self.i = 0
    def __iter__(self):
        return self
    def __next__(self):
        while True:
            self.i += 1
            if self.i == self.end:
                raise StopIteration()
            if self.i % 2 == 0:
                return (self.i)

spisok = EvenNumbers(0, 25)
for i in spisok:
    print(i)