import DisjointSet as dst

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = []

    def addEdge(self, s, d, w):
        self.graph.append([s, d, w])

    def addNode(self, value):
        self.nodes.append(value)

    def printSolution(self):
        for s, d, w, in self.MST:
            print("%s - %s: %s" % (s, d, w))

    def kruskalAlgo(self):
        cost = 0
        ds = dst.DisjointSet(self.nodes)
        self.graph = sorted(self.graph, key=lambda item: item[2]) # sorting based on value present at index 2
        for g_item in self.graph:
            x = ds.find(g_item[0])
            y = ds.find(g_item[1])
            if x!= y:
                self.MST.append(g_item)
                ds.union(x, y)
                cost += g_item[2]
        self.printSolution()
        print("Total Cost : ", cost)

g = Graph(5)
g.addNode("A")
g.addNode("B")
g.addNode("C")
g.addNode("D")
g.addNode("E")
g.addEdge("A", "B", 5)
g.addEdge("A", "C", 13)
g.addEdge("A", "E", 15)
g.addEdge("B", "A", 5)
g.addEdge("B", "C", 10)
g.addEdge("B", "D", 8)
g.addEdge("C", "A", 13)
g.addEdge("C", "B", 10)
g.addEdge("C", "E", 20)
g.addEdge("C", "D", 6)
g.addEdge("D", "B", 8)
g.addEdge("D", "C", 6)
g.addEdge("E", "A", 15)
g.addEdge("E", "C", 20)

g.kruskalAlgo()