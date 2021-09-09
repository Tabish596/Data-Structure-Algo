class sorting:
    def __init__(self, arr):
        self.arr = arr

    def selectionsort(self):
        for i in range(len(self.arr)):
            minindex = i
            for j in range(i+1, len(self.arr)):
                if self.arr[j] < self.arr[minindex]:
                    minindex = j
            self.arr[i], self.arr[minindex] = self.arr[minindex], self.arr[i]
        print('This is Selection Sorted', self.arr)
        return

    def bubblesort(self):
        while True:
            swap = 0
            for i in range(len(self.arr)-1):
                if self.arr[i] > self.arr[i+1]:
                    self.arr[i], self.arr[i+1] = self.arr[i+1], self.arr[i]
                    swap = 1
            if swap == 0:
                print('This is Bubble Sorted', self.arr)
                return

    def insertionsort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i-1
            while (j >= 0 and key < self.arr[j]):
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
        print('This is insertion Sorted', self.arr)
        return

    def mergesort(self, p):
        if len(p) < 2:
            return p
        mid = len(p)//2
        left = p[:mid]
        right = p[mid:]
        return(self.merge(self.mergesort(left), self.mergesort(right)))

    def merge(self, l, r):
        result = []
        i, j = 0, 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        return (result+l[i:]+r[j:])


if __name__ == '__main__':
    s = sorting([8, 2, 4, 3, 9])
    s.selectionsort()
    # s.bubblesort()
    # s.insertionsort()
    #print(s.mergesort([4, 2, 6, 1, 9]))
