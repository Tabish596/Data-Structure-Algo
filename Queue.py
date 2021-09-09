class node:
    def __init__(self,data):
        self.value = data
        self.next = None
class queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def printqueue(self):
        temp = self.first
        while(temp):
            print(temp.value)
            temp = temp.next
    def peek(self):
        print(self.first)
    def enqueue(self,data):
        new = node(data)
        if self.length == 0 :
            self.first = new
            self.last = new
            self.length +=1
            return
        self.last.next = new
        self.last = new
        self.length+=1
    def dequeue(self):
        temp = self.first
        self.first = temp.next
        temp = None

if __name__ == '__main__':
    newqueue = queue()
    newqueue.enqueue(5)
    newqueue.enqueue(8)
    newqueue.enqueue(50)
    newqueue.enqueue(15)
    newqueue.enqueue(2)
    newqueue.enqueue(4)
    newqueue.dequeue()
    newqueue.enqueue(19)
    newqueue.printqueue()



