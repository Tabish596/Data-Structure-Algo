class searching:
    def __init__(self, arr):
        self.arr = arr

    def linearsearch(self, a):
        for i in range(len(self.arr)):
            if self.arr[i] == a:
                print('Element found')
                return
        print('Element not fount')

    def mergesort(self, p):
        if len(p) < 2:
            return p
        mid = len(p)//2
        left = p[0:mid]
        right = p[mid:]
        return(self.merge(self.mergesort(left), self.mergesort(right)))

    def merge(self, l, r):
        result = []
        i = 0
        j = 0
        while i < len(l) and j < len(r):
            if l[i] < r[j]:
                result.append(l[i])
                i += 1
            else:
                result.append(r[j])
                j += 1
        return(result+l[i:]+r[j:])

    def Binarysearch(self, a):
        sorted = self.mergesort(self.arr)
        while True:
            mid = len(sorted)//2
            if sorted[mid] == a:
                print('Element found at', mid)
                return
            elif a > sorted[mid] and len(sorted) > 1:
                sorted = sorted[mid:]
            elif a < sorted[mid] and len(sorted) > 1:
                sorted = sorted[0:mid]
            else:
                print('element not found')
                return


if __name__ == '__main__':
    s = searching([4, 1, 7, 3, 2, 9, 5, 4, 6])
    # s.Binarysearch(3)
