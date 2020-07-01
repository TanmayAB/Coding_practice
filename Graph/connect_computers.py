#n = 6
#connections = [[0,1],[0,2],[0,3],[1,2],[1,3]] # 2
#n = 6
#connections = [[0,1],[0,2],[0,3],[1,2]] # -1
n = 5
connections = [[0,1],[0,2],[3,4],[2,3]] # 0

def makeConnected(n, connections):
    
    disjoint_map = {}

    class DisJointSet:
        rank = None
        data = None
        parent = None

    def makeSet(data):
        node = DisJointSet()
        node.data = data
        node.rank = 0
        node.parent = node
        disjoint_map[data] = node

    def find(node):
        if node.parent != node:
            node.parent = find(node.parent)
        return node.parent

    def union(data1, data2):
        node1 = disjoint_map[data1]
        node2 = disjoint_map[data2]

        parent1 = find(node1)
        parent2 = find(node2)

        if parent1.parent == parent2.parent:
            return 1
        
        if parent1.rank >= parent2.rank:
            if parent1.rank == parent2.rank:
                parent1.rank += 1
            parent2.parent = parent1
        else:
            parent1.parent = parent2
        
        return 0
    
    redundant = 0
    for i in range(0, len(connections)):
        j, k = connections[i]

        if j not in disjoint_map:
            makeSet(j)
        if k not in disjoint_map:
            makeSet(k)

        redundant += union(j,k)
    
    if redundant >= n - len(disjoint_map.keys()):
        return redundant
    else:
        return -1

print("Ans : ", makeConnected(n, connections))


