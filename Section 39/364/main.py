import sys
class Graph:
    def __init__(self, vertexNum, edges, nodes):
        self.edges = edges
        self.nodes = nodes
        self.vertexNum = vertexNum
        self.MST = []

    def printSolution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def primsAlgo(self):
        visted = [0]*self.vertexNum
        edgeNum = 0
        visted[0] = True
        while edgeNum<self.vertexNum-1: # when number of edges in MST will be one less than number of nodes
            min = sys.maxsize # initially min set to infinity
            for i in range(self.vertexNum):
                if visted[i]:
                    for j in range(self.vertexNum):
                        if ((not visted[j]) and self.edges[i][j]):
                            if min > self.edges[i][j]:
                                min = self.edges[i][j]
                                s = i
                                d = j
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visted[d] = True
            edgeNum += 1
        self.printSolution()

edges = [
    [0, 10, 20, 0, 0], # distance of node A to all nodes
    [10, 0, 30, 5, 0], # distance of node B to all nodes
    [20, 30, 0, 15, 6],
    [0, 5, 15, 0, 8],
    [0, 0, 6, 8, 0]
]

nodes = ["A", "B", "C", "D", "E"]
g = Graph(5, edges, nodes)
g.primsAlgo()