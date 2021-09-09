class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    def push(self,data):
        new = node(data)
        new.next = self.head
        self.head = new
    def append(self,data):
        new = node(data)
        if self.head==None:
            self.head = new
            self.tail = new
            return
        self.tail.next = new
        self.tail = new

    def insert_after(self,data,index):
        new = node(data)
        pos = self.head
        n=0
        while(n<index):
            pos = pos.next
            n+=1
        new.next = pos.next
        pos.next = new
    def delete(self,index):
        pos = self.head
        n = 0
        if index == 0:
            self.head = pos.next
            pos = None
            return
        while(n<index):
            temp = pos
            if pos.next == None:
                return(print("Wrong Index of Deletion"))
            pos = pos.next
            n+=1
        temp.next = pos.next
        pos = None


if __name__ == '__main__' :
    llist = linkedlist()
    llist.append(3)
    llist.append(6)
    llist.push(2)
    llist.push(7)
    llist.append(3)
    llist.insert_after(23,2)
    llist.delete(0)
    llist.printlist()

