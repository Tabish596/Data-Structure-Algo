class graphs:
    def __init__(self):
        self.numberofnodes = 0
        self.adjacentList = {}

    def addvertex(self, node):
        self.adjacentList[node] = []

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)


if __name__ == '__main__':
    g = graphs()
    g.addvertex(0)
    g.addvertex(1)
    g.addvertex(2)
    g.addvertex(3)
    g.addvertex(4)
    g.addvertex(5)
    g.addvertex(6)
