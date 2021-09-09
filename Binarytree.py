class node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
class binarytree:
    def __init__(self):
        self.root = None
    def insert(self,data):
        new = node(data)
        if self.root==None:
            self.root = new
            return
        current = self.root
        while True:
            if new.value>current.value:
                if current.right == None:
                    current.right = new
                    return
                current = current.right
            else:
                if current.left == None:
                    current.left = new
                    return
                current = current.left
    def lookup(self,data):
        current = self.root
        while True:
            if data == current.value:
                print('Available')
                return
            if data > current.value and current.right:
                current = current.right
            elif data < current.value and current.left:
                current = current.left
            else: 
                print('Not found')
                return

if __name__ == '__main__':
    btree = binarytree()
    btree.insert(25)
    btree.insert(5)
    btree.insert(7)
    btree.insert(45)
    btree.insert(15)
    btree.insert(52)
    btree.insert(13)
    btree.insert(6)
    btree.insert(33)
    btree.lookup(18)