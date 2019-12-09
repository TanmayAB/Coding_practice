from pprint import pprint as pp

class Graph:
    V = set()
    adj_list = {}

    def addEdge(self, u, v):
        if u not in self.adj_list:
            self.V.add(u)
            self.V.add(v)
            self.adj_list[u] = []
        self.adj_list[u].append(v)
    
    def printGraph(self):
        print(" Vertices: {}".format(self.V))
        print("Adj. List: ")
        pp(self.adj_list)

    def topologicalSort(self):
        stack = []
        visited = []
        
        for v in self.V:
            if v not in visited:
                self.topoUtil(v, visited, stack)
        while stack:
            pp(stack.pop())
            pp('->')
    def topoUtil(self, u, visited, stack):
        if u in visited:
            return
        visited.append(u)
        if u in self.adj_list:
            for v in self.adj_list[u]:
                self.topoUtil(v, visited, stack)
        stack.append(u)

g = Graph()
g.addEdge('A', 'B')
g.addEdge('B', 'C')
g.addEdge('C', 'E')
g.addEdge('B', 'D')
g.addEdge('D', 'F')
g.addEdge('E', 'H')
g.addEdge('E', 'F')
g.addEdge('F', 'G')
g.printGraph()
g.topologicalSort()
