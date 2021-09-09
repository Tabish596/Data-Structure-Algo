class node:
    def __init__(self,value):
        self.value = value
        self.next = None
class stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        if self.top is not None:
            print(self.top)
            return
    def push(self,data):
        new = node(data)
        if self.length == 0:
            self.bottom = new
            self.top = new
            self.length+=1
            return
        new.next = self.top
        self.top = new
        self.length+=1
    def pop(self):
        temp = self.top
        self.top = temp.next
        temp = None
        self.length-=1
    def printst(self):
        temp = self.top
        while(temp):
            print(temp.value)
            temp = temp.next

if __name__ == '__main__':
    nstack = stack()
    nstack.push(15)
    nstack.push(6)
    nstack.push(1)
    nstack.push(8)
    nstack.pop()
    nstack.printst()
        
