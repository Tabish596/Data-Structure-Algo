class manipulation:
    def __init__(self):
        self.length = 0
        self.array = []
        self.temp = [0]
    def get(self,index):
        return(self.array[index])
    def phoos(self,dat):
        self.array = self.array + self.temp
        self.array[self.length]=dat
        self.length += 1
    def poop(self):
        self.array = self.array[:self.length-1]
        self.length -=1
    def deet(self,dat):
        r = self.array.index(dat)
        self.moveside(r)
        self.length-=1
    def moveside(self,index):
        for i in range(index,self.length-1):
            self.array[i]=self.array[i+1]
        self.array = self.array[:self.length-1]
        return(self.array)
""" x = manipulation()
x.phoos('hi')
x.phoos('how')
x.phoos('are')
x.phoos('you')
x.phoos('bro')
#x.poop()
x.deet('are')
print(x.array) """